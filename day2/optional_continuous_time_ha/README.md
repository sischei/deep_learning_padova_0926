# Optional: continuous-time heterogeneous agents

**This material is not taught in the two days.** It is included for anyone who wants to take the
PINN machinery from [Session 8](../code/08_pinns) and [Session 9](../code/09_pinns_applications)
all the way to a general-equilibrium heterogeneous-agent model.

Everything here is complete and runnable — it simply did not fit in ten hours.

## What it covers

| File | Contents |
|---|---|
| [`Continuous_Time_HA.pdf`](Continuous_Time_HA.pdf) | 26 slides: the HJB and Kolmogorov-forward system; Itô essentials; Aiyagari in continuous time mapped operator by operator to its discrete-time analog; the master equation; upwind finite differences (Achdou–Han–Lasry–Lions–Moll) against a PINN on the same problem, and when finite differences stop being viable. |
| [`Aiyagari_Continuous_Time_FD_and_PINN.ipynb`](Aiyagari_Continuous_Time_FD_and_PINN.ipynb) | The coupled HJB–KFE system for continuous-time Aiyagari, solved both ways and compared. GPU recommended; `RUN_MODE = "smoke"` runs on a laptop CPU. |
| [`ss-torch-how-it-works-2026-06-10.md`](ss-torch-how-it-works-2026-06-10.md) | How the PyTorch steady-state solver works, for reading the implementation closely. |

## Where to start

1. Session 9's [`09_03_PE_Discrete_HJB_PINN.ipynb`](../code/09_pinns_applications/09_03_PE_Discrete_HJB_PINN.ipynb)
   is the natural bridge — one agent's HJB with an income process, solved by finite differences and
   by a PINN. Understand that first.
2. Then the slides here, for the step from partial to general equilibrium: the distribution becomes
   a state, and the KFE joins the HJB.
3. Then the Aiyagari notebook.

## Reading

- Achdou, Han, Lasry, Lions & Moll (2022), *Income and Wealth Distribution in Macroeconomics: A
  Continuous-Time Approach*, *Review of Economic Studies* 89(1), 45–86 — the finite-difference benchmark.
- Payne's lecture notes in [`../readings/Payne_continuous_time`](../readings/Payne_continuous_time):
  stochastic calculus, the Kolmogorov forward equation, solving differential equations, optimal
  control, equilibrium, and the Krusell–Smith master equation.
- Gu, Laurière, Merkel & Payne (2024), *Global Solutions to Master Equations*, arXiv:2406.13726.
- Chapter 8 of [`../../companion_script.pdf`](../../companion_script.pdf).

The notebook is written with Pavel Ievlev; the solver is a port of the JAX code behind Gu et al. (2024).
