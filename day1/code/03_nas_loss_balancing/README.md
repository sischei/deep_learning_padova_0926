# Session 3, Neural architecture search and loss balancing

Day 1, 13:30–14:25. Slides: [`03a_Neural_Architecture_Search.pdf`](../../slides/03a_Neural_Architecture_Search.pdf) · [`03b_Loss_Balancing.pdf`](../../slides/03b_Loss_Balancing.pdf)

The engineering session. Sessions 4 and 5 both lean on it: cohort-stacked OLG residuals and the
IRBC's country-by-country Euler equations are exactly the multi-component losses that need balancing,
and every policy network in those sessions has a width and a learning rate somebody had to pick.

| Notebook | What it does | Runtime |
|---|---|---|
| [`03_01_Grid_vs_Random_Search.ipynb`](03_01_Grid_vs_Random_Search.ipynb) | Where to put a fixed number of trials. Measures the grid-versus-random edge as a function of dimension and of how inert the spare axes are (Bergstra & Bengio, 2012), then checks it on a real network, including the case where the grid wins. | 10 min (teaching), 3 min (smoke) |
| [`03_02_NAS_RandomSearch_Hyperband.ipynb`](03_02_NAS_RandomSearch_Hyperband.ipynb) | How to spend a fixed number of epochs. Random search and successive halving with continuation, in pure Python, with a train / validation / test split and three seeds. Section 7 runs the same search on the Brock–Mirman DEQN of Session 2 with the Euler error as the score. | 29 min from scratch (teaching), 2 min from the cache, 2 min (smoke) |
| [`03_03_Loss_Normalization.ipynb`](03_03_Loss_Normalization.ipynb) | The scale problem in multi-equation losses, with the gradient each component sends measured per epoch. Natural units, inverse-loss weighting, ReLoBRaLo (per epoch and per step) compared over three seeds; then the same measurement on the Session 2 labour model. | 12 min |

Timings measured on a laptop CPU at the committed `RUN_MODE = "teaching"`. The stored outputs are
those runs, so nothing has to be re-executed to read the numbers. **In class, set `RUN_MODE = "smoke"`
first**; the sweeps in `03_02` are cached per preset in `nas_results/`, so both the smoke and the
teaching preset load their sweep from disk and run in about two minutes. Delete a cache file to re-run its sweep.

## What the stored runs say

**`03_02`, architecture search.** Genz Gaussian on $[0,1]^2$, train / validation / test 1,000 / 1,000 / 2,000,
three seeds per method. Best validation loss, median over seeds (range):

| method | epochs paid | median best validation loss | range |
|---|---:|---:|---|
| hand-picked 3×64 ReLU, 100 epochs | 100 | 9.8·10⁻⁶ | |
| random search, 30 trials × 50 epochs | 1,500 | **3.2·10⁻⁶** | 1.8·10⁻⁶ – 3.7·10⁻⁶ |
| successive halving, 27 → 9 → 3 → 1, continued | 504 | 6.7·10⁻⁶ | 6.4·10⁻⁶ – 1.1·10⁻⁵ |

Random search is ahead on all three seeds; successive halving got within a factor of two for a third
of the epochs. The winner retrained from scratch has a test MAE of 0.0016 against 0.0029 for the
baseline. Grouping all 90 random trials by one hyperparameter at a time: activation separates the
levels by 241×, depth by 197×, the learning-rate decade by 23×, mean width by 6×.

On the Brock–Mirman DEQN (30 random trials, 3,000 episodes each, score = mean |relative Euler error|
on 4,096 held-out states): best 2.4·10⁻⁴ (3×32 tanh, lr 2·10⁻³), the `02_02` default (2×50 ReLU,
lr 3·10⁻⁴) 2.1·10⁻³, worst 7.9·10⁻³. Width moved the median score 3.5×, depth 2.2×, the
learning-rate decade and the activation about 1.5×.

**`03_03`, loss balancing.** Three Genz targets at scales 1, 10², 10⁴ behind one shared trunk, 500
epochs, three seeds. Total relative error (sum over the three components of mean |error| / scale),
median over seeds:

| rule | median | range |
|---|---:|---|
| equal weights | 0.861 | 0.833–0.924 |
| inverse-loss weighting | 0.448 | 0.418–0.609 |
| ReLoBRaLo, one update per epoch | 0.861 | 0.833–0.933 |
| ReLoBRaLo, one update per optimizer step | 0.871 | 0.832–0.931 |
| residuals divided by their scale, equal weights | **0.012** | 0.008–0.018 |

Under equal weights the large-scale component sends a gradient 7,000 times the small one's. ReLoBRaLo
is indistinguishable from equal weighting at every temperature in the sweep, per epoch because the
smoothing never lets the weights move, per step because it balances progress, not scale. On the
Session 2 labour model the gap between the two first-order conditions is 1.2·10⁵ in gradient norm at
a random initial policy and gone by episode 300: a transient gap, which equal weights survive and
inverse-loss weighting shortens (and, in relative form, over-corrects).

The hands-on exercise that applies inverse-loss weighting to a real model is
[`05_03_IRBC_Exercise.ipynb`](../05_irbc/05_03_IRBC_Exercise.ipynb) in Session 5; it needs the IRBC
model first.
