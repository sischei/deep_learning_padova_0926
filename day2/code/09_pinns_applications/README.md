# Session 9, Economics-informed neural networks: applications and hands-on

Day 2, 15:10–16:00. Slides: [`09_PINNs_Applications.pdf`](../../slides/09_PINNs_Applications.pdf) · [`10_Wrap_Up.pdf`](../../slides/10_Wrap_Up.pdf)

Part II of the PINN block, building on the method from [Session 8](../08_pinns).

| Notebook | What it does | Runtime |
|---|---|---|
| [`09_01_Cake_Eating_HJB_PINN.ipynb`](09_01_Cake_Eating_HJB_PINN.ipynb) | The first economic application: the cake-eating HJB with a scaled hard-BC trial solution, Adam → L-BFGS in FP64, checked against the closed form. | ~3 min |
| [`09_02_Black_Scholes_PINN.ipynb`](09_02_Black_Scholes_PINN.ipynb) | European call pricing against the Black–Scholes closed form; the Greeks come for free by automatic differentiation. | ~3 min |
| [`09_03_PE_Discrete_HJB_PINN.ipynb`](09_03_PE_Discrete_HJB_PINN.ipynb) | A step beyond cake-eating: partial-equilibrium HJB with a two-state income chain, solved by an upwind finite-difference scheme **and** by a PINN, so the two can be compared. | ~4 min |
| [`09_04_PINN_Exercise.ipynb`](09_04_PINN_Exercise.ipynb) | **Hands-on, in class.** Build a PINN from scratch for u'' + u = 0 on [0, π]. Fill-in-the-blank, with solutions after each task so you can finish it afterwards. | ~15 min in class |
