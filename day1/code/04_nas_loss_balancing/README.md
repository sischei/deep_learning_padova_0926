# Session 4 — Neural architecture search and loss balancing

Day 1, 14:25–15:20. Slides: [`04a_Neural_Architecture_Search.pdf`](../../slides/04a_Neural_Architecture_Search.pdf) · [`04b_Loss_Balancing.pdf`](../../slides/04b_Loss_Balancing.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`04_01_Grid_vs_Random_Search.ipynb`](04_01_Grid_vs_Random_Search.ipynb) | Why random search beats grid search at a fixed budget (Bergstra & Bengio, 2012). | ~2 min, CPU |
| [`04_02_NAS_RandomSearch_Hyperband.ipynb`](04_02_NAS_RandomSearch_Hyperband.ipynb) | Random search and Hyperband (successive halving) implemented in pure Python, on a 10-D search over depth, width, activation and learning-rate decay. Reads cached sweeps from `nas_results/`. | ~5 min, CPU (cached) |
| [`04_03_Loss_Normalization.ipynb`](04_03_Loss_Normalization.ipynb) | The scale problem in multi-equation residual losses; non-dimensionalisation, inverse-loss weighting, and ReLoBRaLo compared head to head. | ~5 min, CPU |
| [`04_04_IRBC_Exercise.ipynb`](04_04_IRBC_Exercise.ipynb) | **Exercise.** Comparative statics on the trained IRBC policy, and inverse-loss weighting in practice. | ~20 min to work through |

`nas_results/search_records.pkl` holds pre-computed sweeps so the search notebook runs in class
without waiting for a full re-search.
