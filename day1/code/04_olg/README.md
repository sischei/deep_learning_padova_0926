# Session 4, OLG models with DEQNs

Day 1, 14:25–15:25. Slides: [`04_OLG_Models_DEQNs.pdf`](../../slides/04_OLG_Models_DEQNs.pdf)

| Notebook | What it does | Teaching preset |
|---|---|---|
| [`04_00_OLG_Diamond_Warmup.ipynb`](04_00_OLG_Diamond_Warmup.ipynb) | **Warm-up.** Diamond's two-period OLG: two cohorts alive at once, one policy, one Euler equation, closed form $s=\beta w/(1+\beta)$. The whole DEQN in sixty lines. | **69 s** |
| [`04_01_OLG_Analytic_DEQN_persistent.ipynb`](04_01_OLG_Analytic_DEQN_persistent.ipynb) | **Start here.** Analytic 6-generation OLG (Krueger & Kübler, 2004), trained on its own ergodic set and validated against the closed-form savings rates. | **11 min** (smoke 2.5 min) |
| [`04_03_OLG_Exercise.ipynb`](04_03_OLG_Exercise.ipynb) | **Exercise.** Closed-form savings rates; simulate to get the model's own ergodic prices; lifecycle profiles at those prices; the discount factor in general equilibrium. Pure NumPy, no network. | seconds to run, ~25 min to work through |
| [`04_04_OLG_Analytic_DEQN_exogenous.ipynb`](04_04_OLG_Analytic_DEQN_exogenous.ipynb) | Ablation: the same model trained on a broad exogenous box instead of the ergodic set. | **3.5 min** |

All timings measured on a laptop CPU, not estimated.

## The shipped outputs are converged runs

`RUN_MODE = "teaching"` is the committed default and the preset the stored outputs came from, so the
numbers and figures you see without running anything are the good ones:

| | loss | mean rel. Euler error | vs the closed form |
|---|---|---|---|
| `04_00` | 1e-06.2 | — | savings fraction within 4.6e-04 on the visited states |
| `04_01` | 1.2e-07 | **0.026%** | savings rates to **1.0e-05**, capital path to 2.0e-04 |
| `04_04` | 2.8e-07 | 0.037% | savings rates to 2.7e-05, capital path to 2.4e-04 |

Both DEQN notebooks report `PASS: policy drift is small`.

**In class, set `RUN_MODE = "smoke"` first.** That is a deliberately unconverged sanity check, and it is
the preset that fits the hands-on slot. Note that smoke is ~2.5 min rather than seconds: the diagnostics
and the 200k-period ergodic-price simulation at the end cost the same at any preset.

The `persistent` / `exogenous` pair is the point: where you draw the training cloud changes the solution
you get. Compare `04_01` against `04_04`, and see [`optional/`](optional/) for the same comparison at
56 cohorts, where the gap is a factor of 1180.

## The 56-cohort benchmark

Part III of the slides covers the two-asset, 56-cohort benchmark of Azinovic, Gaegauf & Scheidegger
(2022). There is no hands-on for it. The reference implementation, including **the paper's trained
network weights**, is upstream:

**<https://github.com/sischei/DeepEquilibriumNets>** → `code/python-scripts/benchmark`

`python benchmark.py` loads those weights and regenerates the paper's figures in seconds. The local
re-cuts are in [`optional/`](optional/), together with the guard bug behind slides III.5 and III.6.
