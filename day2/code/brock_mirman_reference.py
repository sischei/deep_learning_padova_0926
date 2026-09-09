"""Reference solution of the stochastic Brock-Mirman model, by the endogenous grid method.

The model is the one of Session 2 (Day 1): log utility, Cobb-Douglas production with
capital share ALPHA, depreciation DELTA, and an AR(1) for log productivity,

    Y_t = z_t K_t**ALPHA,   K_{t+1} = (1 - DELTA) K_t + s_t Y_t,   C_t = (1 - s_t) Y_t,
    log z_{t+1} = rho log z_t + SIGMA eps_{t+1},   eps ~ N(0, 1).

The discount factor beta and the persistence rho are arguments of every function, because
Sessions 6 and 7 treat them as the parameters to be learned or estimated.

Four functions are exported:

    solve(beta, rho)                      -> Policy, consumption as a function of cash on hand
    simulate(policy, beta, rho, T)        -> Y, C, K paths after a burn-in
    euler_error(policy, beta, rho, z, K)  -> relative Euler-equation errors at given states
    moments(Y, C, K)                      -> the moment vector used by the SMM notebooks

The solver iterates on the Euler equation with cash on hand m = Y + (1 - DELTA) K as the
state (Carroll, 2006): on a grid of next-period capital K', the right-hand side of the Euler
equation is an expectation that needs no root-finding, today's consumption is its reciprocal
(log utility), and today's cash on hand is C + K'. Consumption is stored as a cubic spline
in (m, log z) and the iteration stops when it no longer changes.
"""
import time
import numpy as np
from scipy.interpolate import CubicSpline, RectBivariateSpline

ALPHA, DELTA, SIGMA = 0.36, 0.10, 0.04
N_GH = 5
_gh_x, _gh_w = np.polynomial.hermite.hermgauss(N_GH)
GH_NODES, GH_WEIGHTS = _gh_x * np.sqrt(2.0), _gh_w / np.sqrt(np.pi)

MOMENT_NAMES = ["Std(dlog C)", "Autocorr(dlog C)", "Autocorr(log Y)", "Mean savings rate"]


def steady_state(beta):
    """Deterministic steady state at z = 1: capital and savings rate."""
    k = (ALPHA / (1.0 / beta - 1.0 + DELTA)) ** (1.0 / (1.0 - ALPHA))
    return k, DELTA * k ** (1.0 - ALPHA)


def cash_on_hand(z, K):
    return z * K ** ALPHA + (1.0 - DELTA) * K


def _eval(spline, m_lim, logz_lim, z, m):
    """Spline evaluation with inputs clipped to the grid (no polynomial extrapolation)."""
    lz = np.clip(np.log(z), *logz_lim)
    mm = np.clip(m, *m_lim)
    return spline.ev(mm.ravel(), lz.ravel()).reshape(np.shape(m))


class Policy:
    """Consumption C(m, z) as a cubic spline in (cash on hand, log z); the savings rate
    s(z, K) = (m - C - (1 - DELTA) K) / Y follows. Negative s means dis-saving."""

    def __init__(self, spline, m_lim, logz_lim, beta, rho, n_iter, wall):
        self._spline, self.m_lim, self.logz_lim = spline, m_lim, logz_lim
        self.beta, self.rho, self.n_iter, self.wall = beta, rho, n_iter, wall

    def consumption(self, z, m):
        z, m = np.broadcast_arrays(np.asarray(z, float), np.asarray(m, float))
        return _eval(self._spline, self.m_lim, self.logz_lim, z, m)


    def __call__(self, z, K):
        z, K = np.broadcast_arrays(np.asarray(z, float), np.asarray(K, float))
        y = z * K ** ALPHA
        c = self.consumption(z, cash_on_hand(z, K))
        return (y + (1.0 - DELTA) * K - c - (1.0 - DELTA) * K) / y


def _rhs(consumption, beta, rho, logz, k_next):
    """beta * E[(1 - DELTA + r') / C'] at next-period capital k_next, given today's log z."""
    out = np.zeros_like(k_next)
    for eps, w in zip(GH_NODES, GH_WEIGHTS):
        z1 = np.exp(rho * logz + SIGMA * eps)
        y1 = z1 * k_next ** ALPHA
        c1 = consumption(z1, y1 + (1.0 - DELTA) * k_next)
        out += w * (1.0 - DELTA + ALPHA * y1 / k_next) / c1
    return beta * out


def _interp_linear_tails(x, y, xq):
    """Cubic spline through (x, y) inside [x[0], x[-1]], linear continuation outside."""
    order = np.argsort(x)
    x, y = x[order], y[order]
    cs = CubicSpline(x, y, extrapolate=False)
    out = cs(xq)
    lo, hi = xq < x[0], xq > x[-1]
    out[lo] = y[0] + cs(x[0], 1) * (xq[lo] - x[0])
    out[hi] = y[-1] + cs(x[-1], 1) * (xq[hi] - x[-1])
    return out


def solve(beta, rho, n_k=120, n_z=31, tol=1e-9, max_iter=2000):
    """Endogenous-grid iteration on the Euler equation. Returns a Policy."""
    t0 = time.perf_counter()
    k_ss, _ = steady_state(beta)
    z_sd = SIGMA / np.sqrt(1.0 - rho ** 2)
    logz_grid = np.linspace(-6.0 * z_sd, 6.0 * z_sd, n_z)
    logz_lim = (logz_grid[0], logz_grid[-1])
    k_grid = np.exp(np.linspace(np.log(0.05 * k_ss), np.log(6.0 * k_ss), n_k))     # next-period capital
    m_grid = np.linspace(cash_on_hand(np.exp(logz_grid[0]), 0.05 * k_ss),
                         cash_on_hand(np.exp(logz_grid[-1]), 6.0 * k_ss), 2 * n_k)  # cash on hand
    m_lim = (m_grid[0], m_grid[-1])
    KP, LZ = np.meshgrid(k_grid, logz_grid, indexing="ij")
    M, _ = np.meshgrid(m_grid, logz_grid, indexing="ij")

    C = 0.5 * M                                                       # initial guess: consume half
    spline = RectBivariateSpline(m_grid, logz_grid, C, kx=3, ky=3)
    for it in range(1, max_iter + 1):
        cons = lambda z1, m1: _eval(spline, m_lim, logz_lim, z1, m1)
        c_endo = 1.0 / _rhs(cons, beta, rho, LZ, KP)                  # log utility: C = 1 / RHS
        m_endo = c_endo + KP                                          # today's cash on hand
        C_new = np.column_stack([_interp_linear_tails(m_endo[:, j], c_endo[:, j], m_grid) for j in range(n_z)])
        diff = np.max(np.abs(C_new - C) / C)
        C = C_new
        spline = RectBivariateSpline(m_grid, logz_grid, C, kx=3, ky=3)
        if diff < tol:
            break
    return Policy(spline, m_lim, logz_lim, beta, rho, it, time.perf_counter() - t0)


def simulate(policy, beta, rho, T, seed=0, burn=200, K0=None, z0=1.0):
    """One path of length T after `burn` periods. Returns Y, C, K arrays of length T."""
    rng = np.random.default_rng(seed)
    eps = rng.standard_normal(T + burn)
    K = np.empty(T + burn + 1); z = np.empty(T + burn + 1)
    K[0] = steady_state(beta)[0] if K0 is None else K0
    z[0] = z0
    for t in range(T + burn):
        c_t = policy.consumption(z[t], cash_on_hand(z[t], K[t]))
        K[t + 1] = cash_on_hand(z[t], K[t]) - c_t
        z[t + 1] = np.exp(rho * np.log(z[t]) + SIGMA * eps[t])
    z, K = z[burn:-1], K[burn:-1]
    Y = z * K ** ALPHA
    C = policy.consumption(z, cash_on_hand(z, K))
    return Y, C, K


def euler_error(policy, beta, rho, z, K):
    """Relative Euler-equation error 1 - 1 / (beta C E[(1 - DELTA + r') / C']) at states (z, K)."""
    z, K = np.broadcast_arrays(np.asarray(z, float), np.asarray(K, float))
    m = cash_on_hand(z, K)
    c = policy.consumption(z, m)
    return 1.0 - 1.0 / (c * _rhs(policy.consumption, beta, rho, np.log(z), m - c))


def _autocorr(x):
    x0, x1 = x[:-1] - x[:-1].mean(), x[1:] - x[1:].mean()
    return float(np.sum(x0 * x1) / np.sqrt(np.sum(x0 ** 2) * np.sum(x1 ** 2)))


def moments(Y, C, K):
    """[Std(dlog C), Autocorr(dlog C), Autocorr(log Y), mean investment share] for one path,
    or one row per column if Y, C, K are 2-d arrays (time along axis 0)."""
    Y, C, K = (a.reshape(-1, 1) if a.ndim == 1 else a for a in (Y, C, K))
    dlc = np.diff(np.log(C), axis=0)
    ly = np.log(Y)
    inv_share = 1.0 - C / Y
    out = np.column_stack([dlc.std(axis=0),
                           [_autocorr(dlc[:, j]) for j in range(dlc.shape[1])],
                           [_autocorr(ly[:, j]) for j in range(ly.shape[1])],
                           inv_share.mean(axis=0)])
    return out[0] if out.shape[0] == 1 else out
