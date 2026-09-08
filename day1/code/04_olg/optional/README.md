# Not taught: the 56-cohort AGS (2022) benchmark

These two notebooks are **not part of Session 4**. Part III of the slides presents the model, and the
reference implementation lives upstream:

**<https://github.com/sischei/DeepEquilibriumNets>** → `code/python-scripts/benchmark`

That repository ships the **trained network weights from the paper**. `python benchmark.py` loads them
and regenerates the paper's figures in seconds, with no training; `python benchmark.py
--train_from_scratch` reproduces the full two-stage schedule, which is a GPU job.

## Why these are here and not in the session

They are the record behind slide III.5, "What a failed run looks like".

Shrinking the benchmark to a preset that trains on a laptop in a classroom slot does not work. Four
attempts at two different presets: three diverged, one converged.

| | outcome |
|---|---|
| 201 segments @ lr 2e-4 | loss 3.8e+09, 71% of the cross-section at $c \le 0$ |
| 201 segments @ lr 2e-4, repeat | loss 7.1e+07, 81% at $c \le 0$ |
| 401 segments @ lr 1e-4 | loss 7.2e-03, 0% at $c \le 0$, bond market to 0.09% of output |
| 401 segments @ lr 1e-4, repeat | loss 1.7e+10, 82% at $c \le 0$ |

The failure is always the same: the loss looks healthy for about twenty segments, aggregate $K$ then
splits away from the ergodic range (to 130+ against a feasible box topping out near 70) and never
returns. Since the training cloud *is* the simulation, once it runs away the residual is being
minimised somewhere the economy never visits. Identical settings produced both a converged and a
diverged run, because TensorFlow on CPU is not bit-reproducible and this problem sits close enough to
the edge for that to decide the outcome.

The stored outputs in `04_02` are one of the diverged runs. That is deliberate: it is what the slide
describes.

`04_05` is the exogenous-sampling ablation. It reaches a loss of 2.7e-02 on its own sampling box and
7e+11 on the *simulated* cloud, which is the ablation's whole point, a solution that looks healthy
exactly where it was trained and fails where the economy actually goes.

## What is still worth reading here

The model code itself is correct and matches the slides: the two Euler equations with the
adjustment-cost wedge, the product-form KKT residuals, the bond-market residual, and the policy heads.
Section 3 documents the constraint-head problem (the default head keeps both constraints slack by
construction), and section 4 derives every residual. If you want to read a DEQN for a two-asset,
two-constraint OLG model, read these; if you want to *run* one, use the upstream repository.
