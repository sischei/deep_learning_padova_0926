# Session 4, OLG models with DEQNs

Day 1, 14:25–15:25. Slides: [`04_OLG_Models_DEQNs.pdf`](../../slides/04_OLG_Models_DEQNs.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`04_00_OLG_Diamond_Warmup.ipynb`](04_00_OLG_Diamond_Warmup.ipynb) | **Warm-up.** Diamond's two-period OLG: two cohorts alive at once, one policy, one Euler equation, closed form $s = \beta w/(1+\beta)$. The entire DEQN in sixty lines, validated to four decimals. | ~1 min, CPU |
| [`04_01_OLG_Analytic_DEQN_persistent.ipynb`](04_01_OLG_Analytic_DEQN_persistent.ipynb) | **Start here.** Analytic 6-generation OLG (Krueger & Kübler, 2004), trained on the ergodic set and validated against the closed-form age-specific savings rates. | smoke ~30 s; **teaching ~45 min**, CPU |
| [`04_03_OLG_Exercise.ipynb`](04_03_OLG_Exercise.ipynb) | **Exercise.** Closed-form savings rates; simulate the economy under them to get its ergodic prices; lifecycle profiles at those prices, and the discount factor in general equilibrium. Pure NumPy, no network. | ~25 min to work through |
| [`04_04_OLG_Analytic_DEQN_exogenous.ipynb`](04_04_OLG_Analytic_DEQN_exogenous.ipynb) | Ablation: the same analytic model trained on a broad exogenous box instead of the ergodic set. | smoke ~30 s; **teaching ~45 min**, CPU |

**Stored outputs are `teaching`-preset runs**, so the numbers and figures you see without running
anything are the converged ones: `04_01` reproduces the closed-form savings rates to $1.4\times10^{-4}$.
`RUN_MODE = "teaching"` is also the committed default. **In class, set it to `"smoke"` first**: a
~30-second sanity check whose numbers are deliberately not converged, and the only preset that fits the
hands-on slot.

The `persistent` / `exogenous` pair is the point: where you draw the training cloud changes the solution
you get. Compare `04_01` against `04_04` directly.

## The 56-cohort benchmark

Part III of the slides covers the 56-cohort, two-asset benchmark of Azinovic, Gaegauf & Scheidegger
(2022), but there is no notebook for it here. The reference implementation, including **the trained
network weights from the paper**, is upstream:

**<https://github.com/sischei/DeepEquilibriumNets>** → `code/python-scripts/benchmark`

`python benchmark.py` loads those weights and regenerates the paper's figures in seconds. The local
re-cuts that would not train at a classroom preset are kept in [`optional/`](optional/), together with
the measurements behind slide III.5.
