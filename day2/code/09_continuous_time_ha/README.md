# Session 9 — Continuous-time heterogeneous agents

Day 2, 15:10–16:00. Slides: [`09_Continuous_Time_HA.pdf`](../../slides/09_Continuous_Time_HA.pdf) · [`10_Wrap_Up.pdf`](../../slides/10_Wrap_Up.pdf)

| Notebook | What it does | Runtime |
|---|---|---|
| [`09_01_PE_Discrete_HJB_PINN.ipynb`](09_01_PE_Discrete_HJB_PINN.ipynb) | **Warm-up.** Partial-equilibrium HJB with a two-state income chain: upwind finite differences and a PINN on the same problem. | ~4 min, CPU |
| [`09_02_Aiyagari_Continuous_Time_FD_and_PINN.ipynb`](09_02_Aiyagari_Continuous_Time_FD_and_PINN.ipynb) | Full general equilibrium: the coupled HJB–KFE system for continuous-time Aiyagari, solved by an upwind FD scheme and by a PINN, compared side by side. | GPU recommended; `smoke` runs on CPU |

[`ss-torch-how-it-works-2026-06-10.md`](ss-torch-how-it-works-2026-06-10.md) documents the PyTorch
steady-state solver used in `09_02`, for anyone who wants to read the implementation closely.

Written with Pavel Ievlev; the solver is a port of the JAX code behind Gu, Laurière, Merkel & Payne (2024).
