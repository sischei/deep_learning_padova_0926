# Session 6, Deep surrogates and Gaussian processes

Day 2, 09:00–09:50. Slides: [`06_Deep_Surrogates_and_GPs.pdf`](../../slides/06_Deep_Surrogates_and_GPs.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`06_01_Surrogate_Primer.ipynb`](06_01_Surrogate_Primer.ipynb) | A deep surrogate of Black–Scholes over (S, K, T, σ, r), then implied-volatility inversion, a controlled benchmark where the right answer is known. | ~4 min, CPU |
| [`06_02_GP_and_BAL.ipynb`](06_02_GP_and_BAL.ipynb) | Gaussian-process regression from scratch and via scikit-learn; Bayesian active learning to choose the next design point. | ~3 min, CPU |

The idea carried into Session 7: treat structural parameters as **pseudo-states**, train once, and the
expensive re-solve inside an estimation loop disappears.
