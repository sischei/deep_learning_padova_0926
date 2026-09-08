# Teaching notes

Internal notes for running the Padova suite. Not part of the student-facing material.

## Where this material came from

Every deck and notebook is drawn from the full-length course. The source decks kept for provenance
live in [`_sources/`](_sources); the tools used to re-cut them are in [`_tools/`](_tools):

* `_tools/section_select.py`, rebuild a shortened deck by keeping a subset of `\section` blocks.
  Dropped sections are left as commented markers, so the result stays diffable against its source.
* `_tools/frame_extract.py`, pull named frames out of a deck by title. Used to build Session 9.
* `_tools/smoke_test.sh`, execute the CPU-light notebooks end to end.

Re-cuts applied:

| Deck | Change |
|---|---|
| `02_DeepEquilibriumNets` | Dropped *Loss Balancing* and *Architecture Search*, these became Session 4, taught from dedicated decks. 77 → 54 frames. |
| `06_Deep_Surrogates_and_GPs` | Dropped *Structural Estimation* (→ Session 7) and *Optimal Carbon Tax* / *Quantify: Uncertainty* (climate; no setup in this course). 75 → 39 frames. |
| `07a_Structural_Estimation_SMM` | The estimation section of the surrogates deck, standing alone. |
| `08_PINNs_Foundations` / `09_PINNs_Applications` | The full 57-frame deck, restored (Black–Scholes back in) and split across the two afternoon slots: sections I–III (36 frames) and IV–VI (25 frames). |
| `Continuous_Time_HA` | **New,** then cut from the taught schedule. 26-frame extract from the two 60-frame continuous-time decks; now optional self-study under `day2/optional_continuous_time_ha/`. |
| `10_Wrap_Up` | **New.** Rewritten for a two-day arc; climate-specific slides replaced. |

## Timing

407 frames across 540 minutes, about 1.33 minutes per frame overall, before hands-on time.

| Session | Frames | Minutes | Pace |
|---|---:|---:|---|
| 1 Intro to DL | 57 | 90 | 1.58 comfortable |
| 2 DEQNs | 54 | 75 | 1.39 comfortable |
| 3 NAS + loss balancing | 56 | 55 | **0.98 tightest** |
| 4 OLG | 39 | 60 | **1.54 the most slack** |
| 5 IRBC | 49 | 50 | 1.02 tight |
| 6 Surrogates + GPs | 39 | 50 | 1.28 comfortable |
| 7 SMM | 42 | 55 | 1.31 comfortable |
| 8 PINNs I, foundations | 36 | 55 | 1.53 comfortable |
| 9 PINNs II, applications | 25 | 30 | 1.20 tight |
| Hands-on (09_04) |, | 12 | at the keyboard |
| Wrap-up | 10 | 8 |, |

**Trim order if running long:** the GradNorm comparison in Session 3 → the Bayesian active-learning
demo in Session 6 → the inverse-problems frames in Session 9.

Sessions 3 and 5 are the ones to watch. Session 3 has the least slack, and it is also the session
where a live demo is most tempting, run `03_02` from its cached `nas_results/` rather than
re-searching.

**On the Day 2 afternoon.** It is two hours of PINNs and nothing else. Continuous-time
heterogeneous agents was originally Session 9 and was cut: fifty minutes was not enough to do the
HJB--KFE system justice straight after a compressed PINN session, and the source deck it came from
runs to 126 frames. The material survives intact as optional self-study. The PINN deck was designed
for ninety minutes, so restoring it in full (Black--Scholes included) and splitting it across two
slots gives both halves more room than anything on Day 1, plus twelve minutes of hands-on at the keyboard.

Session 9 is the tight one in the afternoon at 1.20 min/frame. If it runs over, the Black--Scholes
frames (§V, 6 minutes) are the ones to drop --- notebook `09_02` covers the same ground and students
can run it themselves --- rather than eating into the hands-on block.

**On the OLG session.** Reviewed twice, because OLG is Padova's research focus. The first pass
checked correctness: the mathematics on the slides was right, but the 56-cohort notebook's policy head
kept capital saving bounded away from zero (at 0.0045) and the collateral slack at 8% of it, so neither
constraint could ever bind and both multipliers were trained to zero. The deck gained a two-period
Diamond warm-up (`04_00`), the Euler and closed-form derivations, an explicit sequence-to-recursive
slide, and real teaching-run figures in place of hand-drawn schematics. The exercise's Task 2 now
simulates the model's own ergodic prices (gross $r \approx 0.69$) instead of assuming $r = 0.15$.
IRBC gave up five frames to make room.

The second pass asked whether it *teaches*, and changed more:

* **The DEQN's defining feature was on no slide in the course.** The residual evaluates the network at
  its own successor state, once per shock, so the loss is a fixed-point condition on $\theta$ rather
  than a regression. Session 2's training-step diagram draws a single call and Algorithm 1 writes
  $\rho(s,\mathcal N(s))$. It is now II.7a, with a diagram, placed where the age shift $h \to h+1$
  makes it concrete.
* **Results arrived before their derivations.** II.6 asserted the Euler equation and II.6a then derived
  it; $\beta_h$ was derived at II.6b and re-asserted as a fresh "Claim" five frames later. Merged and
  reordered. II.8/II.8a wrote the same signature twice and never said in words how $f$ differs from
  $\mathcal N_\theta$; merged, with the sentence added.
* **`04_01` shipped stored outputs from a *smoke* run**, showing the DEQN 9 percentage points off the
  closed form with a "policy is still moving" warning, on the one notebook whose entire purpose is
  validation. Re-run at the teaching preset it matches to $1.4\times10^{-4}$. Its teaching preset also
  takes ~45 minutes, not the five that was claimed; corrected in three places.
* **Smaller things:** `\sum_{i=0}^{A-s}` should have been `A-h` (twice); §5's markdown documented a
  `BATCH_SIZE` that does not exist and pseudo-code with the wrong signature (in all four DEQN
  notebooks); `04_03` had its `## Background` block twice and no `## Task 1` heading; the slide loss
  omitted the penalty terms the code minimises; comments now tie the ageing slice, the successor-state
  call, and the two multipliers to the equations they implement.

**Why the 56-cohort benchmark is slides-only.** It does not train at any laptop-scale preset. Four
attempts, three diverged: 201 segments at lr 2e-4 gave losses of 3.8e+09 and 7.1e+07 on two identical
runs (71% and 81% of the cross-section at negative consumption); doubling the segments and halving the
step gave 7.2e-03 once and 1.7e+10 the next time. The failure is always the same, the simulated cloud
runs away past aggregate K of 130 around segment 20 and never returns, so the residual is minimised
where the economy never goes. Identical settings give different outcomes because TensorFlow on CPU is
not bit-reproducible and the problem sits on the edge.

So Part III is now five slides and no notebook: the model, the multipliers, the loss at scale, the
paper's lifecycle profiles, and III.5 on the failure. Students who want to run it are pointed at
`sischei/DeepEquilibriumNets`, `code/python-scripts/benchmark`, which ships the paper's **trained
weights**: `python benchmark.py` regenerates the paper's figures in seconds with no training at all.
That is a better hands-on than the local re-cut ever was. The re-cuts live in
`day1/code/04_olg/optional/` with the measurements behind III.5.

III.5 is worth teaching deliberately. It is a real failure, encountered while preparing this lecture,
and it makes the case for Session 3 (architecture search, loss balancing) better than any argument.

**On the session order.** Architecture search and loss balancing come *before* the two large
applications on purpose: IRBC's country-by-country Euler residuals and the cohort-stacked OLG system
are exactly the multi-component losses that need balancing, so teaching the remedy first means both
applications land on prepared ground. IRBC closes the day as the scaling finale.

## Compute

Notebooks needing a GPU (demo in class, `RUN_MODE = "smoke"` for students on laptops):

* `05_01`, `05_02`, IRBC
* the optional Aiyagari notebook, not taught
* (`04_02` and `04_05` are no longer in the session; see above)

Everything else runs on a laptop CPU in a few minutes, **with one exception measured this pass**:
`04_01` and `04_04` at `RUN_MODE = "teaching"` take about 45 minutes of CPU, not the five that was
claimed before. The persistent notebook spends almost all of it simulating the cloud forward under the
network, 501 segments deep. The stored outputs are that converged run, so nobody has to reproduce it;
in class students should run `"smoke"` (~30 s). The README and slide II.11 now say so.

## Open items

* Confirm room and local contact details with the Padova organizers.
* Decide whether to set the DEQN exercise blanks (`02_03`) as an assessed take-home.
