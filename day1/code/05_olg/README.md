# Session 5 — OLG models with DEQNs

Day 1, 15:35–16:30. Slides: [`05_OLG_Models_DEQNs.pdf`](../../slides/05_OLG_Models_DEQNs.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`05_01_OLG_Analytic_DEQN_persistent.ipynb`](05_01_OLG_Analytic_DEQN_persistent.ipynb) | **Start here.** Analytic 6-generation OLG (Krueger & Kübler, 2004), trained on the ergodic set and validated against closed-form age-specific savings rates. | ~5 min, CPU |
| [`05_02_OLG_Benchmark_DEQN_persistent.ipynb`](05_02_OLG_Benchmark_DEQN_persistent.ipynb) | The 56-cohort production benchmark (Azinovic, Gaegauf & Scheidegger, 2022) with borrowing and collateral constraints via product-form KKT residuals. | GPU recommended |
| [`05_03_OLG_Exercise.ipynb`](05_03_OLG_Exercise.ipynb) | **Exercise.** Closed-form savings rates and lifecycle profiles. | ~20 min to work through |
| [`05_04_OLG_Analytic_DEQN_exogenous.ipynb`](05_04_OLG_Analytic_DEQN_exogenous.ipynb) | Ablation: the same analytic model trained on a broad exogenous box instead of the ergodic set. | ~5 min, CPU |
| [`05_05_OLG_Benchmark_DEQN_exogenous.ipynb`](05_05_OLG_Benchmark_DEQN_exogenous.ipynb) | The same ablation for the 56-cohort benchmark. | GPU recommended |

The `persistent` / `exogenous` pair is the point: where you draw the training cloud changes the
solution you get. Compare `05_01` against `05_04` to see it directly.
