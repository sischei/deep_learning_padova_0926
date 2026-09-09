# Session 9, Physics-informed neural networks: applications and hands-on

Day 2, 15:10–16:00. Slides: [`09_PINNs_Applications.pdf`](../../slides/09_PINNs_Applications.pdf) · [`10_Wrap_Up.pdf`](../../slides/10_Wrap_Up.pdf)

Part II of the PINN block, building on the method from [Session 8](../08_pinns). Every notebook
measures the network against a reference: a closed form where one exists, a finite-difference
solution where it does not. All notebooks are PyTorch, CPU-only, and run in double precision.

| Notebook | What it does | Stored result | Runtime |
|---|---|---|---|
| [`09_01_Cake_Eating_HJB_PINN.ipynb`](09_01_Cake_Eating_HJB_PINN.ipynb) | The first economic application. Forward problem: the cake-eating HJB with a trial solution whose endpoint values are exact, Adam then L-BFGS, checked against the closed form. Inverse problem: the discount rate $\rho$ is unknown, consumption is observed at 20 wealth levels, and $\rho$ is recovered together with $V$ in one optimisation. | forward: consumption within 4.3e-3 of $\kappa a$ (relative $L^2$ error 1.1e-3); inverse: $\hat\rho$ = 0.0500 from a start at 0.08, 0.0495 with 1 % noise | ~1 min |
| [`09_02_Black_Scholes_PINN.ipynb`](09_02_Black_Scholes_PINN.ipynb) | European call pricing against the Black–Scholes closed form; Delta and Gamma by automatic differentiation from the same network. Self-study. | price within 0.06 of the closed form at $t=0$ (mean 0.03); Delta within 0.01, Gamma within 0.003 of a 0.044 peak | ~1 min |
| [`09_03_PE_Discrete_HJB_PINN.ipynb`](09_03_PE_Discrete_HJB_PINN.ipynb) | A consumption-savings problem with a borrowing constraint and a two-state income chain, solved by an upwind finite-difference scheme and by a PINN, so the two can be compared. The finite-difference scheme converges in 13 iterations; the PINN reaches a small residual and a consumption policy 26 % off, and the notebook explains how to tell and why. Self-study. | PINN value functions within 3 %, consumption relative $L^2$ error 0.26, residual 2e-3 RMS | ~1 min |
| [`09_04_PINN_Exercise.ipynb`](09_04_PINN_Exercise.ipynb) | **Hands-on, 12 minutes in class.** Build a PINN from scratch for $u'' + u = 0$ on $[0, \pi/2]$ with $u(0) = 0$, $u(\pi/2) = 1$. Fill-in-the-blank with a solution after each task. Bonus at home: hard boundary conditions, and why the same equation on $[0,\pi]$ with zero boundary values is ill-posed. | soft 3.2e-4, hard 6.7e-5; the ill-posed variant converges to $u \equiv 0$ with a loss of 1.4e-6 | 30 s |

The figures on the slides (`day2/slides/figures/pinn_*.pdf`) are written by these notebooks; the
stored outputs are the runs the slides quote.
