# Session 3 — Scaling up: IRBC with DEQNs

Day 1, 13:30–14:25. Slides: [`03_IRBC.pdf`](../../slides/03_IRBC.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`03_01_IRBC_DEQN_smooth.ipynb`](03_01_IRBC_DEQN_smooth.ipynb) | The N-country IRBC benchmark: N Euler equations plus the world resource constraint on a 2N-dimensional state. Recovers the symmetric steady state; Euler residuals as the diagnostic. | GPU recommended; `smoke` runs on CPU |
| [`03_02_IRBC_DEQN_irreversible.ipynb`](03_02_IRBC_DEQN_irreversible.ipynb) | The same model with irreversible investment — an occasionally binding constraint handled in the loss. | GPU recommended; `smoke` runs on CPU |

These are the first notebooks where the model is genuinely out of reach for a tensor-product grid.
In class they are demonstrated; set `RUN_MODE = "smoke"` to run them yourself on a laptop.
