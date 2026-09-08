# Session 3 — Neural architecture search and loss balancing

Day 1, 13:30–14:25. Slides: [`03a_Neural_Architecture_Search.pdf`](../../slides/03a_Neural_Architecture_Search.pdf) · [`03b_Loss_Balancing.pdf`](../../slides/03b_Loss_Balancing.pdf)

The engineering session. Sessions 4 and 5 both lean on it: cohort-stacked OLG residuals and the
IRBC's country-by-country Euler equations are exactly the multi-component losses that need balancing.

| Notebook | What it does | Runtime |
|---|---|---|
| [`03_01_Grid_vs_Random_Search.ipynb`](03_01_Grid_vs_Random_Search.ipynb) | Why random search beats grid search at a fixed budget (Bergstra & Bengio, 2012). | ~2 min, CPU |
| [`03_02_NAS_RandomSearch_Hyperband.ipynb`](03_02_NAS_RandomSearch_Hyperband.ipynb) | Random search and Hyperband (successive halving) implemented in pure Python, on a 10-D search over depth, width, activation and learning-rate decay. Reads cached sweeps from `nas_results/`. | ~5 min, CPU (cached) |
| [`03_03_Loss_Normalization.ipynb`](03_03_Loss_Normalization.ipynb) | The scale problem in multi-equation residual losses; non-dimensionalisation, inverse-loss weighting, and ReLoBRaLo compared head to head. | ~5 min, CPU |

`nas_results/search_records.pkl` holds pre-computed sweeps so the search notebook runs in class
without waiting for a full re-search.

The hands-on exercise that applies inverse-loss weighting to a real model is
[`05_03_IRBC_Exercise.ipynb`](../05_irbc/05_03_IRBC_Exercise.ipynb), in Session 5 — it needs the IRBC
model first.
