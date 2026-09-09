# Reading list

*Deep Learning for Solving Dynamic Models, University of Padova, 23–24 September 2026*

The single most useful reference is the companion script,
[`companion_script.pdf`](companion_script.pdf), which covers every method in the course with full
derivations, worked examples and exercise solutions. Everything below is supplementary.

---

## Before the course

* Work through the [Python refresher](python_refresher) and the
  [Jupyter introduction](python_refresher/jupyter_intro.ipynb).
* Fernández-Villaverde, Nuño & Perla (2025), *Taming the Curse of Dimensionality: Quantitative
  Economics with Deep Learning*, [`day1/readings`](day1/readings/Fernandez-Villaverde_Nuno_Perla_2025_Taming_the_Curse_of_Dimensionality.pdf).
  The best single overview of why this literature exists. Read this first.

## Session 1, Introduction to machine learning and deep learning

* Murphy (2022), *Probabilistic Machine Learning: An Introduction*, free PDF at
  [probml.github.io/pml-book](https://probml.github.io/pml-book/book1.html).
  Reference text; Chapters 1, 4 and 13 are the relevant ones.
* James, Witten, Hastie & Tibshirani (2021), *An Introduction to Statistical Learning*, free PDF at
  [statlearning.com](https://www.statlearning.com/).
  Gentler; good on the bias–variance trade-off.
* Companion script, Chapter 1.

## Sessions 2, 5, Deep Equilibrium Nets, and IRBC

* **Azinovic, Gaegauf & Scheidegger (2022)**, *Deep Equilibrium Nets*, *International Economic Review*
  63(4), 1471–1525, [`day1/readings`](day1/readings/Azinovic_Gaegauf_Scheidegger_2022_Deep_Equilibrium_Nets.pdf).
  The core paper for the whole of Day 1 (Sessions 2, 4 and 5).
* Scheidegger & Bilionis (2019), *Machine Learning for High-Dimensional Dynamic Stochastic Economies*,
  [`day1/readings`](day1/readings/Scheidegger_Bilionis_2019_ML_for_HighDim_Dynamic_Stochastic_Economies.pdf).
* Companion script, Chapters 2 and 3.

## Session 3, Architecture search and loss balancing

* Elsken, Metzen & Hutter (2019), *Neural Architecture Search: A Survey*, JMLR 20(55),
  [`day1/readings`](day1/readings/Elsken_Metzen_Hutter_2019_NAS_Survey.pdf).
* Bergstra & Bengio (2012), *Random Search for Hyper-Parameter Optimization*, JMLR 13, 281–305.
* Li, Jamieson, DeSalvo, Rostamizadeh & Talwalkar (2018), *Hyperband: A Novel Bandit-Based Approach to
  Hyperparameter Optimization*, JMLR 18(185), 1–52.
* Bischof & Kraus (2021), *Multi-Objective Loss Balancing for Physics-Informed Deep Learning*
  (ReLoBRaLo), arXiv:2110.09813; published in *Computer Methods in Applied Mechanics and Engineering*
  439, 117914 (2025).
* Wang, Teng & Perdikaris (2021), *Understanding and Mitigating Gradient Flow Pathologies in
  Physics-Informed Neural Networks*, SIAM Journal on Scientific Computing 43(5). The gradient-norm
  view of loss balancing that Notebook `03_03` measures.
* Companion script, Chapter 4.

## Session 4, Overlapping generations

* Diamond (1965), *National Debt in a Neoclassical Growth Model*, *American Economic Review* 55(5),
  1126–1150. The two-period model the session opens with.
* Krueger & Kübler (2004), *Computing Equilibrium in OLG Models with Stochastic Production*,
  *Journal of Economic Dynamics and Control* 28(7), 1411–1436. The closed form used for validation.
* Azinovic, Gaegauf & Scheidegger (2022), §3, the 56-cohort benchmark. Presented on the slides;
  the reference implementation, with the paper's trained weights, is
  [`DeepEquilibriumNets/code/python-scripts/benchmark`](https://github.com/sischei/DeepEquilibriumNets/tree/master/code/python-scripts/benchmark).
* Companion script, Chapter 5.

## Sessions 6–7, Deep surrogates, Gaussian processes, and structural estimation

* **Chen, Didisheim & Scheidegger (2026)**, *Deep Surrogates for Finance: With an Application to Option
  Pricing*, *Journal of Financial Economics* 177, 104222,
  [`day2/readings`](day2/readings/Chen_Didisheim_Scheidegger_2026_Deep_Surrogates_for_Finance_JFE.pdf).
* Rasmussen & Williams (2006), *Gaussian Processes for Machine Learning*,
  [`day2/readings`](day2/readings/Rasmussen_Williams_2006_Gaussian_Processes_for_ML.pdf).
  Chapters 2 and 5 are what the session uses.
* Carroll (2006), *The Method of Endogenous Gridpoints for Solving Dynamic Stochastic Optimization
  Problems*, Economics Letters 91(3), 312–320. The method behind `day2/code/brock_mirman_reference.py`,
  the reference solver that Sessions 6 and 7 validate their surrogates against.
* Scheidegger et al., *Machine Learning for Dynamic Programming*,
  [`day2/readings`](day2/readings/Scheidegger_etal_Machine_Learning_Dynamic_Programming.pdf).
* Companion script, Chapters 9 and 10.

## Sessions 8–9, Physics-informed neural networks

* **Raissi, Perdikaris & Karniadakis (2019)**, *Physics-Informed Neural Networks*, *Journal of
  Computational Physics* 378, 686–707,
  [`day2/readings`](day2/readings/Raissi_Perdikaris_Karniadakis_2019_PINNs.pdf). The founding paper.
* Sirignano & Spiliopoulos (2018), *DGM: A Deep Learning Algorithm for Solving Partial Differential
  Equations*, arXiv:1708.07469.
* Achdou, Han, Lasry, Lions & Moll (2022), *Income and Wealth Distribution in Macroeconomics: A
  Continuous-Time Approach*, Review of Economic Studies 89(1), 45–86. The upwind finite-difference
  scheme that `09_03` uses as its benchmark, and the state-constraint boundary condition.
* Companion script, Chapter 7.
