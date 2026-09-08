# Session 4, OLG models with DEQNs

Day 1, 14:25–15:25. Slides: [`04_OLG_Models_DEQNs.pdf`](../../slides/04_OLG_Models_DEQNs.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`04_00_OLG_Diamond_Warmup.ipynb`](04_00_OLG_Diamond_Warmup.ipynb) | **Warm-up.** Diamond's two-period OLG: one policy, one Euler equation, closed form $s = \beta w/(1+\beta)$. The entire DEQN in sixty lines, validated to four decimals. | ~1 min, CPU |
| [`04_01_OLG_Analytic_DEQN_persistent.ipynb`](04_01_OLG_Analytic_DEQN_persistent.ipynb) | **Start here.** Analytic 6-generation OLG (Krueger & Kübler, 2004), trained on the ergodic set and validated against closed-form age-specific savings rates. | ~5 min, CPU |
| [`04_02_OLG_Benchmark_DEQN_persistent.ipynb`](04_02_OLG_Benchmark_DEQN_persistent.ipynb) | The 56-cohort production benchmark (Azinovic, Gaegauf & Scheidegger, 2022) with borrowing and collateral constraints via product-form KKT residuals. | GPU recommended |
| [`04_03_OLG_Exercise.ipynb`](04_03_OLG_Exercise.ipynb) | **Exercise.** Closed-form savings rates; simulate the economy under them to get its ergodic prices; lifecycle profiles at those prices, and the discount factor in general equilibrium. | ~25 min to work through |
| [`04_04_OLG_Analytic_DEQN_exogenous.ipynb`](04_04_OLG_Analytic_DEQN_exogenous.ipynb) | Ablation: the same analytic model trained on a broad exogenous box instead of the ergodic set. | ~5 min, CPU |
| [`04_05_OLG_Benchmark_DEQN_exogenous.ipynb`](04_05_OLG_Benchmark_DEQN_exogenous.ipynb) | The same ablation for the 56-cohort benchmark. | GPU recommended |

The `persistent` / `exogenous` pair is the point: where you draw the training cloud changes the
solution you get. Compare `04_01` against `04_04` to see it directly.

In the 56-cohort notebooks the default policy head keeps capital saving and the collateral slack
strictly positive, so neither constraint binds and the multipliers are trained to zero; §6 of `04_02`
reports the binding fractions (zero) so this is visible rather than hidden. A head that can reach zero
is available as `CONSTRAINT_HEAD = "bounded_sigmoid"` but does not train at the teaching preset; §3 of
the notebook records what was tried.
