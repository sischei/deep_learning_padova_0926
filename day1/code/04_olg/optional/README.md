# Not taught in the session: the 56-cohort AGS (2022) benchmark

Part III of the slides presents this model. There is no hands-on slot for it, and the reference
implementation lives upstream:

**<https://github.com/sischei/DeepEquilibriumNets>** → `code/python-scripts/benchmark`

That repository ships the **trained network weights from the paper**. `python benchmark.py` loads them
and regenerates the paper's figures in seconds, with no training. `python benchmark.py
--train_from_scratch` reproduces the full two-stage schedule, which is a GPU job.

These two notebooks are the local re-cuts. They train, and their stored outputs are converged runs, but
they do not reach the paper's accuracy and are not worth a classroom slot.

## Measured, `RUN_MODE = "teaching"`, laptop CPU

| | `04_02` persistent | `04_05` exogenous |
|---|---|---|
| wall clock | 49 min | 3 min |
| loss, training cloud | 8.0e-03 | 1.7e-02 |
| loss, simulated (ergodic) cloud | 8.2e-03 | **2.1e+01** |
| mean rel. Euler error, capital | 4.1% | 7.5% on its box, **14.3%** on the ergodic cloud |
| bond market clearing, share of output | 0.14% | 0.12% on its box, **7.1%** on the ergodic cloud |
| share of the cloud with c ≤ 0 | 0% | 0% |
| policy drift | PASS | PASS |

`04_05` is the point of the pair. Trained on a fixed exogenous box it looks healthy *on that box* and is
**1180× worse** on the states the economy actually visits, with a bond market off by 7% of output.
`04_02`, trained on its own simulation, scores the same on both clouds. Where you draw the training
cloud is not a detail.

## The bug behind slide III.5, and why it matters here

Earlier attempts at a classroom-sized preset diverged: three runs out of four reached losses of 1e+07 to
1e+10 with 70–82% of the cross-section at negative consumption, aggregate capital running past 130.

The cause was not the learning rate and not CPU non-determinism. It was this line:

```python
SIM_REPAIR_AGG_K_MAX = 10.0 * N_AGES      # = 560
```

That is the guard which resamples simulated trajectories leaving the feasible region. The notebook's own
sampling box tops out at `EXOGENOUS_K_HIGH * N_AGES` = 70, and a healthy simulated cloud sits at
aggregate capital of roughly 10 to 27. A guard at 560 is eight times the widest state the notebook is
willing to call feasible: it never fired once, in any run, and its `repairs=0` counter was
indistinguishable from a healthy run. Tied to the sampling box, training is stable.

The same bug, a thousand times too loose rather than twenty, was in the taught notebooks `04_01` and
`04_04` (`SIM_REPAIR_AGG_K_MAX = 1.0e3` against an ergodic aggregate capital of 0.93). It never fired
there either and those runs converge regardless, but it offered no protection to a student changing a
preset. Both are fixed.

## What stability does not buy

`04_02` converges but does not solve the model to research accuracy:

* mean relative Euler errors of ~4%, against the ~0.1% of the paper;
* the runaway guard is doing continuous work. It first fires at segment 30 and then resamples
  **about 131 of the 1024 states in every segment, 13% of the training cloud, for the remaining 2970
  segments**. Aggregate capital on the ergodic cloud sits exactly at the bound (69.999 against 70.0).

So the policy is being *held* inside the feasible set rather than settling there, and the cloud it
trains on is partly an artifact of the repair mechanism. Stable is not the same as solved. For the
paper's numbers, use the trained weights upstream.

## What is worth reading here

The model code is correct and matches the slides: the two Euler equations with the adjustment-cost
wedge, the product-form KKT residuals, the bond-market residual, and the policy heads. Section 3
documents the constraint-head limitation (the default head keeps both constraints slack by
construction, so the measured binding fractions are zero), and section 4 derives every residual.
