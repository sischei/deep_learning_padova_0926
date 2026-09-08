# Session 5 — Scaling up: IRBC with DEQNs

Day 1, 15:40–16:30. Slides: [`05_IRBC.pdf`](../../slides/05_IRBC.pdf)

The closing session of Day 1, and the point where a tensor-product grid stops being an option at all.
Session 4 stacked residuals along the *age* dimension; here they stack along a *country* dimension.

| Notebook | What it does | Runtime |
|---|---|---|
| [`05_01_IRBC_DEQN_smooth.ipynb`](05_01_IRBC_DEQN_smooth.ipynb) | The N-country IRBC benchmark: N Euler equations plus the world resource constraint on a 2N-dimensional state. Recovers the symmetric steady state; Euler residuals as the diagnostic. | GPU recommended; `smoke` runs on CPU |
| [`05_02_IRBC_DEQN_irreversible.ipynb`](05_02_IRBC_DEQN_irreversible.ipynb) | The same model with irreversible investment — an occasionally binding constraint handled in the loss. | GPU recommended; `smoke` runs on CPU |
| [`05_03_IRBC_Exercise.ipynb`](05_03_IRBC_Exercise.ipynb) | **Exercise.** Comparative statics on the trained policy, and the inverse-loss weighting from [Session 3](../03_nas_loss_balancing) applied to a model whose residual components genuinely differ in scale. | ~20 min to work through |

In class these are demonstrated; set `RUN_MODE = "smoke"` to run them yourself on a laptop.
