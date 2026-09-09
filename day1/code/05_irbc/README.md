# Session 5, Scaling up: IRBC with DEQNs

Day 1, 15:40–16:30. Slides: [`05_IRBC.pdf`](../../slides/05_IRBC.pdf)

The closing session of Day 1. The model is the international real business cycle model of Brumm and
Scheidegger (2017, *Econometrica*, section 4): N countries with heterogeneous preferences, one world
resource constraint, capital adjustment costs, and (in the second notebook) irreversible investment.
Session 4 stacked residuals along the *age* dimension; here they stack along a *country* dimension.

| Notebook | What it does | Runtime |
|---|---|---|
| [`05_01_IRBC_DEQN_smooth.ipynb`](05_01_IRBC_DEQN_smooth.ipynb) | **Start here.** N = 2, smooth model: N Euler equations plus the world resource constraint on a 2N-dimensional state, trained on simulated states. Policy drift, zero-shock steady state, and a direct comparison with the sparse-grid time-iteration solution. | **3 min** (smoke: under a minute) |
| [`05_02_IRBC_DEQN_irreversible.ipynb`](05_02_IRBC_DEQN_irreversible.ipynb) | The same model with irreversible investment: Kuhn–Tucker multipliers as network outputs, a smoothed Fischer–Burmeister residual in the loss, investment zero by construction where the constraint binds. | **3 min** (smoke: under a minute) |
| [`05_03_IRBC_Exercise.ipynb`](05_03_IRBC_Exercise.ipynb) | **Exercise.** Steady-state comparative statics in the lecture's calibration; inverse-loss weighting on the residual magnitudes `05_02` actually prints; one re-weighted smoke run. | ~30 min to work through |

Timings measured on a laptop CPU. No GPU is needed.

## The shipped outputs are converged runs

`RUN_MODE = "teaching"` is the committed default and the preset the stored outputs came from. **In
class, set `RUN_MODE = "smoke"` first**: under a minute, same code path, residuals an order of magnitude
larger.

| | mean rel. Euler error, ergodic set | max | mean rel. resource error | sanity checks |
|---|---|---|---|---|
| `05_01` | **2.1e-05** | 3.5e-04 | 4.7e-05 | 9 of 9 pass |
| `05_02` | **2.0e-05** | 3.6e-04 | 4.6e-05 | 12 of 12 pass |

Both notebooks end by evaluating the trained network at the same states as an adaptive-sparse-grid
time-iteration solution of the model (see [`reference/`](reference/)). On the sparse grid's own simulated
path, `05_01`'s capital policy differs from the sparse grid's by 8.5e-05 on average (1.5e-03 at worst),
which is investment to within 1 percent of its steady-state level; the two solutions' own Euler errors
there are 2.1e-05 (DEQN) and 2.4e-05 (sparse grid). Away from the ergodic set the DEQN is less accurate
than the sparse grid, because it was never trained there: on the paper's box $[0.8,1.2]^2 \times
[-0.16,0.16]^2$ its mean Euler error is 2.7e-04 against 8.4e-05.

## Where the constraint binds

At this calibration ($\delta = 1\%$ and $\sigma = 1\%$ a quarter) the irreversibility constraint never
binds on the simulated path: neither the sparse grid nor the DEQN has a single binding state there, and
`05_02`'s multipliers stay at zero. On uniform draws from the paper's box the sparse grid binds on
25 percent of (state, country) pairs, in the corners where one country holds far more capital than the
other. The DEQN of `05_02` is trained on simulated states only, yet it binds on 23 percent of the box states and
agrees with the sparse grid on binding against slack for 97 percent of pairs: its head is a smoothed maximum
around the smooth capital choice, so the kink is built in. What it cannot know is the size of the multiplier
there, which is why its Euler error on the box (2.4e-03) is thirty times its error on the ergodic set.
That is why Brumm and Scheidegger evaluate the nonsmooth model on uniform draws over the box.

Training `05_02` with `SAMPLING_MODE = "exogenous"` on the paper's box instead does not help: the
network finds a policy with a mean Euler error of 2.2e-04 on the box whose capital stock explodes under
simulation and whose multiplier on the resource constraint is twice the sparse grid's. The Euler equations
alone admit non-transversal paths; training on the ergodic set is what rules them out. An earlier sigmoid
head for investment, which could approach but never reach zero, plateaued at 2.8e-04 on the ergodic set
and never bound anywhere, even when trained on the box.

## Ten countries

The code is written for general N. With `N_COUNTRIES = 10` (20 states, 21 policies, 22 quadrature
nodes) the same teaching preset trains in 8 minutes on the laptop CPU and reaches a mean relative Euler
error of 8.3e-05 on the ergodic set, with the zero-shock steady state at $k \approx 1.001$ for every
country. The sparse-grid comparison needs N = 2 and is skipped otherwise.
