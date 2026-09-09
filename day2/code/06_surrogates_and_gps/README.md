# Session 6, Deep surrogates and Gaussian processes

Day 2, 09:00–09:50. Slides: [`06_Deep_Surrogates_and_GPs.pdf`](../../slides/06_Deep_Surrogates_and_GPs.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`06_01_Surrogates_The_Idea.ipynb`](06_01_Surrogates_The_Idea.ipynb) | The idea of a surrogate on one concrete case. The expensive model is the stochastic Brock–Mirman economy of Session 2 solved by the reference method (about a second per solve); the quantity of interest is the mean capital stock and investment share as a function of $(\beta, \varrho)$. A Gaussian process and a small network are fit to the same labels and compared on fresh solves as the label budget grows, band coverage included. | 6 min (teaching) |
| [`06_02_GP_Regression.ipynb`](06_02_GP_Regression.ipynb) | Gaussian-process regression from scratch (kernel, prior samples, posterior in two lines), the length scale and noise, scikit-learn with the marginal likelihood, Matérn against squared-exponential on a kink, the two-input surrogate of `06_01` with one length scale per input, and a short active-learning loop. | 28 s (teaching) |

Both notebooks import [`../brock_mirman_reference.py`](../brock_mirman_reference.py), the reference
solver shared with Session 7 (endogenous grid method, cubic splines; relative Euler errors below
$10^{-6}$ on the ergodic set). `06_01` saves its design and labels to `qoi_design.npz`, which `06_02`
reads for its two-input example.

Timings measured on a laptop CPU at the committed `RUN_MODE = "teaching"`. **In class, set
`RUN_MODE = "smoke"` first** (`06_01` about 2.5 min, `06_02` under 20 s; the primer then labels 40 design points and tests on 20).

## What the stored runs say

**`06_01`.** One reference solve takes 1.7 s. Mean capital stock on 60 fresh solves, error relative to its range on the design:

| labels | GP mean | GP max | network mean | network max | GP 95% band coverage (capital / inv. share) |
|---:|---|---|---|---|---|
| 10 | 6.4e-03 | 1.2e-03 | 7.4e-03 | 7.0e-03 | 73% / 78% |
| 20 | 2.9e-03 | 1.9e-04 | 4.1e-03 | 1.4e-03 | 73% / 67% |
| 40 | 1.1e-03 | 5.9e-05 | 3.9e-03 | 5.5e-04 | 92% / 97% |
| 80 | 6.4e-04 | 2.6e-05 | 3.6e-03 | 4.1e-04 | 93% / 95% |
| 160 | 9.9e-05 | 8.2e-06 | 3.0e-03 | 6.0e-04 | 97% / 98% |

The point carried into Session 7: both surrogates are regressions of labels from the solver. The next
session builds a surrogate without labels, a policy network trained on the model's Euler equation with
the parameters as inputs, and simulates it inside an estimator.
