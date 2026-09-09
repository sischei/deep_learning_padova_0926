# Sparse-grid reference solutions for the N = 2 IRBC model

Two CSV files hold the adaptive-sparse-grid time-iteration solution of the model in
Brumm and Scheidegger (2017, *Econometrica*, section 4), evaluated at 2,000 uniform draws
from the paper's state space $[0.8,1.2]^2 \times [-0.16,0.16]^2$ (`set = box`) and at 2,000
states of the solution's own simulated path after a 1,000-period burn-in (`set = ergodic`).

| file | model | grid |
|---|---|---|
| `irbc_n2_smooth_asg.csv` | no irreversibility constraint | local quadratic polynomials, level 3 plus one adaptive refinement (185 points) |
| `irbc_n2_nonsmooth_asg.csv` | irreversible investment | local linear polynomials, level 3 plus one adaptive refinement (389 points) |

Columns: the state `k1, k2, z1, z2`; the policy `kp1, kp2, lam` and, for the nonsmooth
model, the multipliers `mu1, mu2`; consumption `c1, c2`; the solution's own relative Euler
residual under the notebooks' 6-node monomial rule (`ee1_m6, ee2_m6`) and under the code's
19-node degree-5 rule (`ee1_m19, ee2_m19`), the relative resource residual `arc`, and the
paper's binding-aware error of eq. (46), `kkt1_m19, kkt2_m19`. Both time iterations were
run to a policy change below $10^{-7}$ between iterations.

The notebooks `05_01` and `05_02` read these files in their last section and compare the
trained network with the sparse-grid policy at the same states.

## How the files were made

`make_reference.py` is the driver. It runs on a copy of the sparse-grid IRBC code that
accompanies Brumm, Krause, Schaab and Scheidegger (2022), *Sparse Grids for Dynamic Economic
Models*, and needs the Tasmanian library. Two lines of that code were changed for the runs
here:

1. `SOE.py`: consumption is $c_j = (\lambda/\tau_j)^{-\gamma_j}$, the inverse of the planner's
   first-order condition $\tau_j c_j^{-1/\gamma_j} = \lambda$ with $\gamma_j$ the intertemporal
   elasticity of substitution. The shipped file has the exponent $-1/\gamma_j$, which is
   inconsistent with its own welfare weights and makes country 1 consume $A^{16} \approx 10^{-20}$.
2. `parameters.py`: welfare weights $\tau_j = (A - \delta)^{1/\gamma_j}$, so that $\lambda = 1$
   at the deterministic steady state, as in the notebooks. Table II of the paper has
   $A^{1/\gamma_j}$, a normalization carried over from Juillard and Villemot (2011), where
   $\delta = 0$.

With these two changes the solution has $k' = 1$, $\lambda = 1.000$ and $c_j = A - \delta$ for
both countries at $k = 1$, $z = 0$. The redundant interpolation calls in `Expect_FOC.py` were
merged into one for speed; that does not change any number.

```
IRBC_TYPE=smooth     IRBC_DEPTH=3 IRBC_MAXREF=1 IRBC_ORDER=2 IRBC_SURPL=1e-4 IRBC_TOL=1e-7 python make_reference.py irbc_n2_smooth_asg.csv
IRBC_TYPE=non-smooth IRBC_DEPTH=3 IRBC_MAXREF=1 IRBC_ORDER=1 IRBC_SURPL=1e-4 IRBC_TOL=1e-7 python make_reference.py irbc_n2_nonsmooth_asg.csv
```

Each run takes a few minutes on a laptop with `OMP_NUM_THREADS=1`.
