"""
Solve the N=2 IRBC model of Brumm & Scheidegger (2017) by adaptive-sparse-grid time
iteration and export the converged policy on a fixed set of test states.

This is the reference the DEQN notebooks 05_01 / 05_02 compare against.  It runs on a
copy of the sparse-grid code from the "Sparse Grids for Dynamic Economic Models"
handbook chapter, with two changes to that code:

  * SOE.py: consumption is c_j = (lambda/tau_j)**(-gamma_j), the inverse of the planner's
    first-order condition tau_j * c_j**(-1/gamma_j) = lambda for gamma_j the IES.  The
    shipped file has the exponent -1/gamma_j, which makes country 1 consume A**16.
  * parameters.py: tau_j = (A - delta)**(1/gamma_j), so that lambda = 1 at the
    deterministic steady state, as in the notebooks (Table II of the paper has A**(1/gamma_j)).

Usage (needs Tasmanian):
    IRBC_TYPE=smooth      IRBC_DEPTH=3 IRBC_MAXREF=2 IRBC_SURPL=1e-4 python make_reference.py out.csv
    IRBC_TYPE=non-smooth  IRBC_DEPTH=3 IRBC_MAXREF=2 IRBC_SURPL=1e-4 python make_reference.py out.csv
"""
import os, sys, copy, time
import numpy as np
import Tasmanian

from parameters import *
from setup_num_int import *
from setup_asg import *
import time_iteration as time_iter
from aux_fcts import F, Fk, AdjCost, AdjCost_k, AdjCost_ktom

out_csv = sys.argv[1]
t0 = time.time()
print(f"type={typeIRBC} depth={gridDepth} order={gridOrder} maxRef={maxRef} surpl={surplThreshold} tol={tol_ti}")
print(f"A={A_tfp:.6f} tau={pareto}")

# ---------------------------------------------------------------- time iteration
grid0_ = grid0
polGuess_ = polGuess
for iter0 in range(0, maxiter + 1):
    polGuess1 = copy.copy(polGuess_)
    grid1 = time_iter.fresh_grid()
    ilev = gridDepth
    while (grid1.getNumNeeded() > 0) and (ilev <= maxRefLevel):
        grid1 = time_iter.ti_step(grid1, polGuess1, grid0_)
        if iter0 > iterRefStart:
            grid1, polGuess1 = time_iter.refine(grid1)
        ilev += 1
    metric, polGuess_, grid0_ = time_iter.policy_update(grid0_, grid1)
    if iter0 % 10 == 0 or metric < tol_ti:
        print("Iteration: %3d, Grid pts: %5d, Level: %2d, Metric: %.4E, %.0f s" % (iter0, grid0_.getNumPoints(), ilev, metric, time.time() - t0), flush=True)
    if metric < tol_ti:
        break
grid = grid1
grid.write(out_csv.replace(".csv", "_grid.txt"))
print("converged after", iter0, "iterations,", grid.getNumPoints(), "points,", f"{time.time()-t0:.0f} s")

# ---------------------------------------------------------------- helpers
N = nCountries
lo = np.array([kMin] * N + [aMin] * N)
hi = np.array([kMax] * N + [aMax] * N)

def evaluate(states):
    """Policies at states (clipped into the grid box).  Returns kp (n,N), lam (n,), mu (n,N)."""
    s = np.clip(states, lo, hi)
    P = grid.evaluateBatch(s)
    kp = P[:, :N]
    lam = P[:, N]
    if typeIRBC == 'non-smooth':
        mu = np.maximum(0.0, P[:, N + 1:])
    else:
        mu = np.zeros_like(kp)
    return kp, lam, mu

def rule_2d(dim):
    r = np.sqrt(dim); nodes = []; w = []
    for i in range(dim):
        for sgn in (+1, -1):
            e = np.zeros(dim); e[i] = sgn * r; nodes.append(e); w.append(1.0 / (2 * dim))
    return np.array(nodes), np.array(w)

def rule_power(dim):
    # degree-5 monomial rule, as in setup_num_int.py (typeInt = 'monomials_power')
    nodes = [np.zeros(dim)]; w = [2.0 / (2 + dim)]
    r1 = np.sqrt(2 + dim)
    for i in range(dim):
        for sgn in (+1, -1):
            e = np.zeros(dim); e[i] = sgn * r1; nodes.append(e); w.append((4 - dim) / (2 * (2 + dim) ** 2))
    r2 = np.sqrt((2 + dim) / 2.0)
    for i in range(dim):
        for j in range(i + 1, dim):
            for si in (+1, -1):
                for sj in (+1, -1):
                    e = np.zeros(dim); e[i] = si * r2; e[j] = sj * r2; nodes.append(e); w.append(1.0 / (dim + 2) ** 2)
    return np.array(nodes), np.array(w)

def euler_errors(states, nodes, weights):
    """Relative Euler residual per country (paper eq. 43: today's mu omitted) and the
    full-FOC residual (today's mu included), for the grid policy at `states`."""
    n = states.shape[0]
    k = states[:, :N]; z = states[:, N:]
    kp, lam, mu = evaluate(states)
    expect = np.zeros((n, N))
    for q in range(len(weights)):
        eps = nodes[q]
        z_next = rhoZ * z + sigE * (eps[:N][None, :] + eps[N])
        s_next = np.concatenate([kp, z_next], axis=1)
        kpp, lam_next, mu_next = evaluate(s_next)
        mpk = 1.0 - delta + Fk(kp, z_next) - AdjCost_k(kp, kpp)
        expect += weights[q] * (lam_next[:, None] * mpk - (1.0 - delta) * mu_next)
    lhs = lam[:, None] * (1.0 + AdjCost_ktom(k, kp))
    ee_paper = betta * expect / lhs - 1.0
    ee_full = (betta * expect + mu) / lhs - 1.0
    # aggregate resource constraint, relative to aggregate resources
    c = (lam[:, None] / pareto[None, :]) ** (-gamma[None, :])
    res = F(k, z) + (1.0 - delta) * k
    arc = np.sum(res - kp - AdjCost(k, kp) - c, axis=1) / np.sum(res, axis=1)
    ic = 1.0 - kp / ((1.0 - delta) * k)                       # paper eq. (45)
    tot = np.maximum(np.maximum(ee_paper, ic), np.minimum(-ee_paper, -ic))   # paper eq. (46)
    return kp, lam, mu, c, ee_paper, ee_full, arc, ic, tot

# ---------------------------------------------------------------- test states
rng = np.random.default_rng(0)
n_box = 2000
box = lo + (hi - lo) * rng.uniform(size=(n_box, 2 * N))

# ergodic states: simulate under the grid policy with the notebooks' shock process
T_burn, T_keep = 1000, 2000
s = np.array([[1.0] * N + [0.0] * N])
clipped = 0
erg = []
for t in range(T_burn + T_keep):
    kp, lam, mu = evaluate(s)
    eps = rng.standard_normal(N + 1)
    z_next = rhoZ * s[:, N:] + sigE * (eps[:N] + eps[N])
    s = np.concatenate([kp, z_next], axis=1)
    if np.any(s < lo) or np.any(s > hi):
        clipped += 1
    if t >= T_burn:
        erg.append(s[0].copy())
erg = np.array(erg)
print(f"ergodic simulation: {clipped} of {T_burn+T_keep} periods left the grid box")
print("ergodic k range", erg[:, :N].min(0), erg[:, :N].max(0), " z range", erg[:, N:].min(0), erg[:, N:].max(0))

# ---------------------------------------------------------------- export
n6, w6 = rule_2d(N + 1)
n19, w19 = rule_power(N + 1)
rows = []
header = (["set"] + [f"k{j+1}" for j in range(N)] + [f"z{j+1}" for j in range(N)]
          + [f"kp{j+1}" for j in range(N)] + ["lam"] + [f"mu{j+1}" for j in range(N)] + [f"c{j+1}" for j in range(N)]
          + [f"ee{j+1}_m6" for j in range(N)] + [f"ee{j+1}_m19" for j in range(N)] + ["arc"] + [f"kkt{j+1}_m19" for j in range(N)])
for name, X in (("box", box), ("ergodic", erg)):
    kp, lam, mu, c, ee6, _, arc, ic, _ = euler_errors(X, n6, w6)
    _, _, _, _, ee19, _, _, _, tot19 = euler_errors(X, n19, w19)
    for i in range(X.shape[0]):
        rows.append([name] + list(X[i]) + list(kp[i]) + [lam[i]] + list(mu[i]) + list(c[i]) + list(ee6[i]) + list(ee19[i]) + [arc[i]] + list(tot19[i]))
    print(f"{name:8s} |Euler| m6  mean {np.abs(ee6).mean():.2e} max {np.abs(ee6).max():.2e} | m19 mean {np.abs(ee19).mean():.2e} max {np.abs(ee19).max():.2e} | log10 mean {np.log10(np.abs(ee19).mean()):.2f} log10 max {np.log10(np.abs(ee19).max()):.2f}")
    print(f"{name:8s} |ARC| mean {np.abs(arc).mean():.2e} max {np.abs(arc).max():.2e} | KKT err (eq.46) mean {np.abs(tot19).mean():.2e} max {np.abs(tot19).max():.2e}")
    if typeIRBC == 'non-smooth':
        binding = (ic > -1e-6)
        print(f"{name:8s} share of (state,country) pairs with I=0: {binding.mean():.4f}; mu>0: {(mu>1e-8).mean():.4f}; min I/k {(-ic*(1-delta)).min():.2e}")
ss = evaluate(np.array([[1.0] * N + [0.0] * N]))
print("steady state check: k'=", ss[0][0], " lambda=", ss[1][0], " c=", (ss[1][0] / pareto) ** (-gamma), " (A-delta=", A_tfp - delta, ")")
import csv
with open(out_csv, "w", newline="") as f:
    wr = csv.writer(f); wr.writerow(header); wr.writerows(rows)
print("wrote", out_csv, len(rows), "rows;", f"{time.time()-t0:.0f} s total")
