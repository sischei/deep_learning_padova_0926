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

404 frames across 540 minutes, about 1.34 minutes per frame overall, before hands-on time.

| Session | Frames | Minutes | Pace |
|---|---:|---:|---|
| 1 Intro to DL | 57 | 90 | 1.58 comfortable |
| 2 DEQNs | 54 | 75 | 1.39 comfortable |
| 3 NAS + loss balancing | 56 | 55 | **0.98 tightest** |
| 4 OLG | 36 | 60 | **1.67 the most slack** |
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
  validation. It now ships a two-stage teaching run: savings rates match the closed form to
  $1.0\times10^{-5}$, mean relative Euler error $2.6\times10^{-4}$, drift PASS.
* **Every runtime claim in this repo was wrong and is now measured.** The "~45 minutes" I briefly put
  on the slides came from a log contaminated by a laptop suspend: one 2314-second gap between segments
  30 and 40, against ~0.35 s/segment everywhere else. Measured: `04_00` 69 s, `04_01` 11 min teaching
  and 2.5 min smoke, `04_04` 3.5 min, `04_02` 49 min. Smoke is minutes rather than seconds because the
  diagnostics and the 200k-period ergodic-price simulation cost the same at any preset.
* **Smaller things:** `\sum_{i=0}^{A-s}` should have been `A-h` (twice); §5's markdown documented a
  `BATCH_SIZE` that does not exist and pseudo-code with the wrong signature (in all four DEQN
  notebooks); `04_03` had its `## Background` block twice and no `## Task 1` heading; the slide loss
  omitted the penalty terms the code minimises; comments now tie the ageing slice, the successor-state
  call, and the two multipliers to the equations they implement.

**Why the 56-cohort benchmark is slides-only, and the bug that nearly hid it.** Early attempts at a
classroom-sized preset diverged: three runs of four reached losses of 1e+07 to 1e+10, with 70-82% of
the cross-section at negative consumption and aggregate capital past 130. The tempting diagnosis was
CPU non-determinism plus a knife-edge problem; halving the learning rate to test it did not help.

The actual cause was `SIM_REPAIR_AGG_K_MAX`, the guard that resamples simulated trajectories leaving
the feasible region. It was set to `10 * N_AGES` = 560 against a sampling box topping out at 70 and a
healthy simulated cloud of roughly 10 to 27, so eight times the widest state the notebook itself calls
feasible. It never fired once, in any run, and a dead guard's `repairs=0`
looks exactly like a healthy one. Tied to the sampling box, training is stable: drift PASS, zero
negative consumption, loss 8.0e-03. **The same bug, a thousand times too loose rather than twenty, was
in the taught `04_01` and `04_04`** (`1.0e3` against an ergodic K of 0.93). It never fired there either
and those runs converge regardless, but it protected nothing. Both are fixed and both still report
`repairs=0`, so shipped behaviour is unchanged.

Stability is not accuracy, and the slides say so: `04_02` still has ~4% mean Euler errors against the
paper's 0.1%, and the guard resamples ~13% of the training cloud in every segment from segment 30 to
segment 3000, with aggregate capital pinned at the bound (69.999 against 70.0). The policy is held
inside the feasible set rather than settling there, so the cloud it trains on is partly an artifact of
the repair mechanism. Part III is therefore three slides, model, multipliers and loss at scale, with
students pointed at `sischei/DeepEquilibriumNets`, `code/python-scripts/benchmark`, which ships the
paper's **trained weights**: `python benchmark.py` regenerates the paper's figures in seconds. The
re-cuts live in `day1/code/04_olg/optional/`.

Three further Part III slides were written and then cut on Simon's call: lifecycle profiles from the
laptop run, and two on the failed run and its diagnosis. The diagnosis is recorded here and in
`optional/README.md` instead. The lesson still holds for anyone who hits it, watch the state
distribution rather than the loss, but it does not earn class time in a sixty-minute session.

**Still open elsewhere, not touched in this pass.** IRBC (`05_01`, `05_02`) has the same shape of
looseness at ~5x rather than 1000x, so it would still catch a genuine runaway, but its segment logs
print no `repairs=` counter at all: there is no way to tell from the committed outputs whether that
guard has ever fired. `05_01`'s stored diagnostics also contain a `FAIL capital fixed point`.

**Audit pass on the OLG session, for correctness, coherence and generated-sounding prose.** Slides:
the hand-over map named `compute_cost()`, which does not exist (`compute_residuals()`); II.10 claimed
training stops when the loss falls below a target, which no notebook does; II.5 indexed the initial
capital holdings $h=1..A-1$ when the cohorts holding capital are $h=2..A$; III.3 quoted the notebook's
input dimension (240) for what is now a description of the paper (236); cash-on-hand was $W$ on two
slides and $\text{inc}$ on four. All fixed, along with the informal phrasing I had put on III.1, III.2,
III.3 and II.7a. The bridge slide to Session 5 was cut on Simon's call; the deck ends on the references.

Notebooks: `04_04`'s sections 6 and 7 were byte-copies of `04_01`'s and described segment continuation
and repairs that the exogenous notebook does not perform; a preset comment said "two hours" for a run
that takes nine minutes; `04_03` had $k'_h$ where it needs $k'^{h+1}$; the README wrote a loss as
`1e-06.2` and a 20,000-period simulation as 200k. The markdown of all four taught notebooks was
rewritten: no meta-commentary about the notebook, no listicle summaries, the word "cloud" (which is
not in AGS 2022) replaced by what is meant in each place, sections renumbered 1-10, notation matched to
the slides. Outputs are untouched; every edit is source-only.

**The finding worth remembering.** The README sold `04_01` versus `04_04` as showing that "where you
draw the training states changes the solution". At six cohorts it does not: the box-trained `04_04`
reaches $3.7\times10^{-4}$ mean Euler error on the ergodic set against `04_01`'s $2.5\times10^{-4}$, in
68 s instead of 539 s, and is 22x better on the box. The box was chosen to contain the ergodic set, so of
course it works. The lesson is now stated correctly in both READMEs and in `04_00` and `04_04`: a box
works when you already know where the ergodic set is; at 56 cohorts nobody does, the box misses it by a
factor of 1180 on the states the economy visits, and simulation is what finds it.

**On the session order.** Architecture search and loss balancing come *before* the two large
applications on purpose: IRBC's country-by-country Euler residuals and the cohort-stacked OLG system
are exactly the multi-component losses that need balancing, so teaching the remedy first means both
applications land on prepared ground. IRBC closes the day as the scaling finale.

## Compute

Notebooks needing a GPU (demo in class, `RUN_MODE = "smoke"` for students on laptops):

* `05_01`, `05_02`, IRBC
* the optional Aiyagari notebook, not taught
* (`04_02` and `04_05` are no longer in the session; see above)

Everything else runs on a laptop CPU in minutes. Measured for Session 4: `04_00` 69 s, `04_01` 11 min
at the teaching preset and 2.5 min at smoke, `04_04` 3.5 min, `04_02` 49 min (not taught). The stored
outputs are the teaching runs, so nobody has to reproduce them; in class students run `"smoke"`.

## Open items

* Confirm room and local contact details with the Padova organizers.
* Decide whether to set the DEQN exercise blanks (`02_03`) as an assessed take-home.
