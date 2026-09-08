# Session 8, Economics-informed neural networks: foundations

Day 2, 14:00–14:55. Slides: [`08_PINNs_Foundations.pdf`](../../slides/08_PINNs_Foundations.pdf)

Part I of the PINN block. This session builds the method; [Session 9](../09_pinns_applications)
after the break applies it. All notebooks are PyTorch, CPU-only and self-contained.

| Notebook | What it does | Runtime |
|---|---|---|
| [`08_01_ODE_PINN_ZeroBCs.ipynb`](08_01_ODE_PINN_ZeroBCs.ipynb) | The smallest complete PINN: y'' = −1 with zero Dirichlet boundary conditions. Everything else in the block is a variation on this. | ~1 min |
| [`08_02_ODE_PINN_SoftVsHardBCs.ipynb`](08_02_ODE_PINN_SoftVsHardBCs.ipynb) | The same ODE with a soft penalty versus a hard trial solution, the central design choice in PINNs. | ~2 min |
| [`08_03_PDE_PINN_Poisson2D.ipynb`](08_03_PDE_PINN_Poisson2D.ipynb) | The 2-D Poisson equation, with hard boundary conditions built by transfinite interpolation. | ~3 min |
