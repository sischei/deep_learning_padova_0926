# Session 8 — Economics-informed neural networks (PINNs)

Day 2, 14:00–14:55. Slides: [`08_PINNs.pdf`](../../slides/08_PINNs.pdf)

All PyTorch, all CPU-only, no file I/O.

| Notebook | What it does | Runtime |
|---|---|---|
| [`08_01_ODE_PINN_ZeroBCs.ipynb`](08_01_ODE_PINN_ZeroBCs.ipynb) | The smallest complete PINN: y'' = −1 with zero Dirichlet boundary conditions. | ~1 min |
| [`08_02_ODE_PINN_SoftVsHardBCs.ipynb`](08_02_ODE_PINN_SoftVsHardBCs.ipynb) | The same ODE with a soft penalty versus a hard trial solution — the central design choice. | ~2 min |
| [`08_03_Cake_Eating_HJB_PINN.ipynb`](08_03_Cake_Eating_HJB_PINN.ipynb) | The cake-eating HJB with a scaled hard-BC trial solution; Adam → L-BFGS in FP64. | ~3 min |
| [`08_04_PINN_Exercise.ipynb`](08_04_PINN_Exercise.ipynb) | **Exercise.** Build a PINN for u'' + u = 0 on [0, π] from scratch; fill-in-the-blank with solutions. | ~30 min |

**Self-study**

| Notebook | What it does |
|---|---|
| [`08_05_PDE_PINN_Poisson2D.ipynb`](08_05_PDE_PINN_Poisson2D.ipynb) | 2-D Poisson with hard BCs via transfinite interpolation. |
| [`08_06_Black_Scholes_PINN.ipynb`](08_06_Black_Scholes_PINN.ipynb) | European call pricing, Greeks by automatic differentiation. |
