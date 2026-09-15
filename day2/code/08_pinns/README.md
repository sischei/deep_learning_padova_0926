# Session 8, Physics-informed neural networks (PINNs) for economics: foundations

Day 2, 10:45–12:00. Slides: [`08_PINNs_Foundations.pdf`](../../slides/08_PINNs_Foundations.pdf)

Part I of the PINN block. A PINN is a neural network trained to satisfy a differential equation:
the residual of the equation, evaluated by automatic differentiation at collocation points, is the
loss. This session builds the method on equations whose solutions are known, so every number is
checked against an exact answer; [Session 9](../09_pinns_applications) after the break applies it.
All notebooks are PyTorch, CPU-only, self-contained, and run in double precision.

| Notebook | What it does | Stored result | Runtime |
|---|---|---|---|
| [`08_01_ODE_PINN_ZeroBCs.ipynb`](08_01_ODE_PINN_ZeroBCs.ipynb) | The smallest complete PINN: $y'' = -1$ with zero boundary values, a boundary penalty, Adam only. Shows that the error of a soft-boundary run is the boundary error carried into the interior. | max error 6.5e-4, of which the boundary miss explains all but 1.2e-4 | 15 s |
| [`08_02_ODE_PINN_SoftVsHardBCs.ipynb`](08_02_ODE_PINN_SoftVsHardBCs.ipynb) | The same equation with non-zero boundary values, solved with a soft penalty and with a hard trial solution, same seed and schedule. Then the second optimizer stage, L-BFGS on a fixed set of points, and single against double precision. | after Adam 3.5e-4 (soft) vs 1.0e-5 (hard); after L-BFGS 3.2e-6 vs 2.6e-7; float32 stalls at 6.8e-7 | 35 s |
| [`08_03_PDE_PINN_Poisson2D.ipynb`](08_03_PDE_PINN_Poisson2D.ipynb) | The 2-D Poisson equation with a manufactured solution; hard boundary conditions on all four sides by transfinite interpolation, against a soft penalty, same schedule. Self-study. | relative $L^2$ error 1.4e-4 (soft) vs 3.7e-6 (hard), a factor 38; the hard run's boundary error is 1e-16 | ~10 min |

The figures on the slides (`day2/slides/figures/pinn_*.pdf`) are written by these notebooks; the
stored outputs are the runs the slides quote.
