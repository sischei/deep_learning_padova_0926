# Session 2 — Deep Equilibrium Nets: the method and Brock–Mirman

Day 1, 10:45–12:00. Slides: [`02_DeepEquilibriumNets.pdf`](../../slides/02_DeepEquilibriumNets.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`02_01_Brock_Mirman_1972_DEQN.ipynb`](02_01_Brock_Mirman_1972_DEQN.ipynb) | Deterministic Brock–Mirman solved with a hand-built DEQN, validated against the closed form `s* = αβ`. | ~2 min, CPU |
| [`02_02_Brock_Mirman_Uncertainty_DEQN.ipynb`](02_02_Brock_Mirman_Uncertainty_DEQN.ipynb) | Adds productivity shocks; Gauss–Hermite quadrature for the conditional expectation in the Euler equation. | ~4 min, CPU |
| [`02_03_DEQN_Exercises_Blanks.ipynb`](02_03_DEQN_Exercises_Blanks.ipynb) | **Exercise.** Endogenous labour, and constraints via KKT with Fischer–Burmeister complementarity. | ~20 min to work through |
| [`02_04_DEQN_Exercises_Solutions.ipynb`](02_04_DEQN_Exercises_Solutions.ipynb) | Full solutions to the above. | — |
| [`02_05_StochasticBM_LossComparison.ipynb`](02_05_StochasticBM_LossComparison.ipynb) | Six loss kernels (MSE, MAE, Huber, pinball, CVaR, log-cosh) on the same setup. | ~5 min, CPU |

All notebooks expose `RUN_MODE = "smoke" | "teaching" | "production"` in the first cell; `smoke` bounds
epochs and sample sizes for a low-spec laptop.
