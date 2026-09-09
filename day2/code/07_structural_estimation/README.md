# Session 7, Structural estimation via SMM

Day 2, 10:05–11:00. Slides: [`07_Structural_Estimation_SMM.pdf`](../../slides/07_Structural_Estimation_SMM.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`07_01_SMM_One_Parameter.ipynb`](07_01_SMM_One_Parameter.ipynb) | Estimate the persistence $\varrho$ of the Brock–Mirman model by the simulated method of moments. The data are one 500-period sample from the reference solution at $\varrho = 0.90$. A policy network with $\varrho$ as an input is trained on the Euler equation, checked against the reference solution at four values of $\varrho$, simulated under common random numbers for 99 candidates, and the criterion is minimized on the fly. The reference solver's own criterion is drawn on a coarse grid for comparison, and the other route is run as well: one Gaussian process per moment fit to those eight reference solves, minimized in place of the simulation. | 3 min (teaching) |
| [`07_02_SMM_Two_Parameters.ipynb`](07_02_SMM_Two_Parameters.ipynb) | The same with $(\beta, \varrho)$ jointly: a four-input network checked at five parameter pairs, two criterion surfaces (dynamic moments only, and with the mean investment share), the joint estimate by a bounded quasi-Newton method, the moment Jacobian's singular values as the identification diagnostic, and the GP route on a 24-point Latin-hypercube design of reference solves. | 8 min (teaching) |

Both notebooks import [`../brock_mirman_reference.py`](../brock_mirman_reference.py), the shared
reference solver. It generates the data, validates the surrogate, and draws the criterion the true
model would give; it is never inside the estimation loop.

Timings measured on a laptop CPU at the committed `RUN_MODE = "teaching"`. **In class, set
`RUN_MODE = "smoke"` first** (`07_01` about 1 min, `07_02` about 3 min). The smoke preset trains a rough surrogate on purpose: the accuracy table then shows consumption errors of a few per cent and the estimate lands off the truth, which is the point of the table.

## What the stored runs say

**`07_01`.** Surrogate against the reference solution on 2,000 ergodic states:

| ϱ | mean Euler error | max | mean consumption error | max |
|---:|---|---|---|---|
| 0.5 | 1.6e-04 | 2.9e-04 | 8.3e-04 | 1.3e-03 |
| 0.7 | 5.5e-05 | 1.4e-04 | 2.1e-04 | 4.9e-04 |
| 0.9 | 1.1e-04 | 1.7e-04 | 5.7e-04 | 7.1e-04 |
| 0.99 | 2.5e-04 | 4.6e-03 | 1.1e-03 | 2.1e-02 |

Estimate ϱ̂ = 0.8793 against 0.90 from a 500-period sample; the surrogate's criterion on 99 candidates lies on the reference solver's on 8 candidates.

**`07_02`.** Surrogate against the reference solution at five parameter pairs (mean / max consumption error): (0.92, 0.5) 4.2e-04 / 7.6e-04, (0.92, 0.99) 5.9e-04 / 3.0e-03, (0.96, 0.9) 9.8e-05 / 5.3e-04, (0.99, 0.5) 2.3e-03 / 2.9e-03, (0.99, 0.99) 3.7e-03 / 3.3e-02. Estimates: dynamic moments only (0.9641, 0.8786), all four moments (0.9605, 0.8782), truth (0.96, 0.90). Singular values of the moment Jacobian: 0.273 and 0.0320 with dynamic moments only (ratio 9, flattest direction (-1.00, -0.01) in (β, ϱ)), 0.272 and 0.1419 with all four (ratio 2).
