# Session 4 — OLG models with DEQNs

Day 1, 14:25–15:15. Slides: [`04_OLG_Models_DEQNs.pdf`](../../slides/04_OLG_Models_DEQNs.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`04_01_OLG_Analytic_DEQN_persistent.ipynb`](04_01_OLG_Analytic_DEQN_persistent.ipynb) | **Start here.** Analytic 6-generation OLG (Krueger & Kübler, 2004), trained on the ergodic set and validated against closed-form age-specific savings rates. | ~5 min, CPU |
| [`04_02_OLG_Benchmark_DEQN_persistent.ipynb`](04_02_OLG_Benchmark_DEQN_persistent.ipynb) | The 56-cohort production benchmark (Azinovic, Gaegauf & Scheidegger, 2022) with borrowing and collateral constraints via product-form KKT residuals. | GPU recommended |
| [`04_03_OLG_Exercise.ipynb`](04_03_OLG_Exercise.ipynb) | **Exercise.** Closed-form savings rates and lifecycle profiles. | ~20 min to work through |
| [`04_04_OLG_Analytic_DEQN_exogenous.ipynb`](04_04_OLG_Analytic_DEQN_exogenous.ipynb) | Ablation: the same analytic model trained on a broad exogenous box instead of the ergodic set. | ~5 min, CPU |
| [`04_05_OLG_Benchmark_DEQN_exogenous.ipynb`](04_05_OLG_Benchmark_DEQN_exogenous.ipynb) | The same ablation for the 56-cohort benchmark. | GPU recommended |

The `persistent` / `exogenous` pair is the point: where you draw the training cloud changes the
solution you get. Compare `04_01` against `04_04` to see it directly.
