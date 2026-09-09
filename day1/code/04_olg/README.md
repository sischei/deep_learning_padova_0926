# Session 4, OLG models with DEQNs

Day 1, 14:25–15:25. Slides: [`04_OLG_Models_DEQNs.pdf`](../../slides/04_OLG_Models_DEQNs.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`04_00_OLG_Diamond_Warmup.ipynb`](04_00_OLG_Diamond_Warmup.ipynb) | **Warm-up.** Diamond's two-period OLG: two cohorts alive at once, one policy, one Euler equation, closed form $a=\beta w/(1+\beta)$. | **69 s** |
| [`04_01_OLG_Analytic_DEQN_persistent.ipynb`](04_01_OLG_Analytic_DEQN_persistent.ipynb) | **Start here.** Analytic 6-generation OLG (Krueger & Kübler, 2004), trained on its own ergodic set and validated against the closed-form savings rates. | **11 min** (smoke 2.5 min) |
| [`04_03_OLG_Exercise.ipynb`](04_03_OLG_Exercise.ipynb) | **Exercise.** Closed-form savings rates; simulate to get the model's own ergodic prices; lifecycle profiles at those prices; the discount factor in general equilibrium. Pure NumPy, no network. | seconds to run, ~25 min to work through |
| [`04_04_OLG_Analytic_DEQN_exogenous.ipynb`](04_04_OLG_Analytic_DEQN_exogenous.ipynb) | The same model trained on states drawn from a fixed box instead of simulated under the policy. | **3.5 min** |

Timings measured on a laptop CPU.

## The shipped outputs are converged runs

`RUN_MODE = "teaching"` is the committed default and the preset the stored outputs came from, so the
numbers and figures you see without running anything are the good ones:

| | loss | mean rel. Euler error | vs the closed form |
|---|---|---|---|
| `04_00` | 6.2e-07 | — | savings fraction within 4.7e-04 on the visited states |
| `04_01` | 1.2e-07 | **0.025%** | savings rates to **1.0e-05**, mean capital-path error 2.0e-04 |
| `04_04` | 2.8e-07 | 0.037% | savings rates to 2.7e-05, mean capital-path error 2.4e-04 |

Both DEQN notebooks report `PASS: policy drift is small`.

**In class, set `RUN_MODE = "smoke"` first.** That is a short run whose numbers are not converged, and
it is the preset that fits the hands-on slot. Smoke takes about 2.5 minutes rather than seconds, because
the diagnostics and the 20,000-period ergodic-price simulation at the end cost the same at any preset.

`04_01` and `04_04` differ in one thing: where the training states come from, simulated under the
current policy or drawn from a fixed box. At six cohorts both work, because the box was chosen to contain
the ergodic set; `04_04` even trains faster. The two ways of sampling come apart when the ergodic set is
not known in advance. At 56 cohorts ([`optional/`](optional/)) the box-trained network is a factor of
1180 worse on the states the economy actually visits.

## The 56-cohort benchmark

Part III of the slides covers the two-asset, 56-cohort benchmark of Azinovic, Gaegauf & Scheidegger
(2022). There is no hands-on for it. The reference implementation, including **the paper's trained
network weights**, is upstream:

**<https://github.com/sischei/DeepEquilibriumNets>** → `code/python-scripts/benchmark`

`python benchmark.py` loads those weights and regenerates the paper's figures in seconds. The local
re-cuts are in [`optional/`](optional/), together with the guard bug that made them look unsolvable.
