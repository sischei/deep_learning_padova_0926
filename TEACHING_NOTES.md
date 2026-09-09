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
| `02_DeepEquilibriumNets` | Dropped *Loss Balancing* and *Architecture Search*, these became Session 3, taught from dedicated decks. 77 → 54 frames. |
| `06_Deep_Surrogates_and_GPs` | Dropped *Structural Estimation* (→ Session 7) and *Optimal Carbon Tax* / *Quantify: Uncertainty* (climate; no setup in this course). 75 → 39 frames. |
| `07_Structural_Estimation_SMM` | Rewritten for Padova around two notebooks; the old exercise deck `07b` is folded in. |
| `08_PINNs_Foundations` / `09_PINNs_Applications` | The full-length PINN deck split across the two afternoon slots, sections I–III and IV–VI. Reviewed in September 2026: every notebook rebuilt around a reference (closed form or finite differences), figures written by the stored runs, the two DGM detail frames dropped, an inverse-problem run and the borrowing-constraint comparison added. |
| `10_Wrap_Up` | **New.** Rewritten for a two-day arc; climate-specific slides replaced. |

## Timing

379 frames across 540 minutes, about 1.42 minutes per frame overall, before hands-on time.

| Session | Frames | Minutes | Pace |
|---|---:|---:|---|
| 1 Intro to DL | 57 | 90 | 1.58 comfortable |
| 2 DEQNs | 54 | 75 | 1.39 comfortable |
| 3 NAS + loss balancing | 56 | 55 | **0.98 tightest** |
| 4 OLG | 36 | 60 | 1.67 comfortable |
| 5 IRBC | 49 | 50 | 1.02 tight |
| 6 Surrogates + GPs | 29 | 50 | 1.72 comfortable |
| 7 SMM | 26 | 55 | **2.12 the most slack** |
| 8 PINNs I, foundations | 36 | 55 | 1.53 comfortable |
| 9 PINNs II, applications | 26 | 30 | 1.15 tight |
| Hands-on (09_04) |, | 12 | at the keyboard |
| Wrap-up | 10 | 8 |, |

**Trim order if running long:** the GradNorm frame in Session 3 → the finger exercise in Session 6 → the
inverse-problems frames in Session 9.

Sessions 3 and 5 are the ones to watch. Session 3 has the least slack, and it is also the session
where a live demo is most tempting: `03_02` loads its sweeps from `nas_results/` for both the smoke
and the teaching preset, so a live run shows the plots in under a minute; do not delete the caches
in class.

**On the Day 2 afternoon.** It is two hours of PINNs and nothing else. Continuous-time
heterogeneous agents was originally Session 9 and was cut: fifty minutes was not enough to do the
HJB--KFE system justice straight after a compressed PINN session, and the source deck it came from
runs to 126 frames. The extract was kept for a while as optional self-study and then removed from the repository to keep it focused. The PINN deck was designed
for ninety minutes, so restoring it in full (Black--Scholes included) and splitting it across two
slots gives both halves more room than anything on Day 1, plus twelve minutes of hands-on at the keyboard.

Session 9 is the tight one in the afternoon at 1.15 min/frame. If it runs over, the Black--Scholes
frames (§V, 6 minutes) are the ones to drop, notebook `09_02` covers the same ground and students
can run it themselves, rather than eating into the hands-on block. Keep the borrowing-constraint
frames: they are the honest half of the case for PINNs, and the hands-on exercise ends on the same
point (its Bonus B is an ill-posed problem the network solves with a loss of $10^{-6}$).

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

**IRBC pass, correctness against Brumm and Scheidegger (2017) and a DEQN that converges.** The
derivations on the slides match the paper line by line: the Euler equation with the adjustment-cost
wedge on both sides and the $(1-\delta)\mu'$ term (their eq. 28), the consumption-sharing condition and
the resource constraint (eq. 30), the adjustment-cost derivatives, and the KKT conditions (eq. 29). Two
deliberate deviations are now stated on the slides: the Pareto weights are $c_{ss}^{1/\gamma_j}$ rather
than the paper's $A^{1/\gamma_j}$ (so that $\lambda_{ss} = 1$ with $\delta > 0$), and the relative Euler
residual keeps $\mu_t$ in the numerator where the paper's eq. (43) drops it. What was wrong on the
slides: every notebook reference said "04a/04b"; the parameter-count table was computed for 64-unit
layers while the architecture slide says 128; the convergence table was placeholders; the hand-over
slide named `compute_cost`; the model was attributed to AGS (2022) and the benchmark literature to
Krueger and Kübler (2004); the finger exercise asked students to verify in the notebook a fall in $k_{ss}$
that the notebook's normalization rules out; the bridge slide claimed N = 10 works without anyone
having run it.

The notebooks were the larger problem. `05_01`'s stored run failed three of its own checks and had a
mean Euler error of 1.7e-3, because it made 1,500 Adam updates at a flat 2e-4, because the committed
`RUN_MODE` ("smoke") did not match the stored outputs ("teaching"), and because its "simulated
evaluation states" started from a wide box with a 64-period burn-in, so they were transition paths, not
the ergodic set. Both notebooks were rebuilt from shared templates: teaching preset with 8,020 updates
under a three-stage learning-rate schedule (1e-3, 1e-4, 1e-5), growth cap 0.1 per quarter, runaway
guard tied to the sampling box with a `repairs=` count in every log line (zero in every stored run),
evaluation on the ergodic set after a 512-period burn-in and on the paper's box, and a final section
that loads a sparse-grid time-iteration solution of the same model and compares policies at the same
states. `05_01` now: mean relative Euler error 2.1e-5 on the ergodic set, all checks pass, 3 minutes
on the laptop, capital policy within 8.5e-5 of the sparse grid on the sparse grid's own path. Ten
countries with the same code: 8 minutes, 8.3e-5. `05_02`'s sigmoid investment head sat deep in its
tail at $I/k = \delta$ and plateaued at 2.8e-4; it was replaced by a smoothed maximum around the smooth
head: $k' = (1-\delta)k + \mathrm{softplus}_s(\tilde k - (1-\delta)k)$ with $s = 10^{-3}k$, so that investment
can be exactly zero and the head has the smooth model's gradient wherever the constraint is slack. `05_02`
now matches `05_01` on the ergodic set (2.0e-5) and passes all twelve checks in 3 minutes.

The sparse-grid reference is Simon's own time-iteration code from the `crest_comp_econ` repository, run
on a scratch copy with one bug fixed: `SOE.py` inverts the consumption first-order condition with the
exponent $-1/\gamma_j$ where the welfare weights in `parameters.py` require $-\gamma_j$, so as shipped
country 1 consumes $A^{16}$ and the stored solutions are a one-consumer economy ($\lambda_{ss} = 0.62$
in `data_smooth/ARC_policy.txt`, against 1.39 for the consistent model). The same line is in every copy
of that code in the lecture repositories, including `HDMR/IRBC/IRBC.py`. Nothing in those repositories
was changed; `day1/code/05_irbc/reference/README.md` documents the fix and how to reproduce the CSVs.

On binding: at this calibration the irreversibility constraint never binds on the simulated path, in
either method. On uniform draws over the paper's box the sparse grid binds on 25 percent of
(state, country) pairs; a DEQN trained on simulated states does not bind there, because it never sees
those states. With the smoothed-maximum head the DEQN nevertheless binds on 23 percent of the box
states and agrees with the sparse grid on binding against slack for 97 percent of pairs, because the kink
is in the head; the multipliers there are untrained, so its box Euler error is 2.4e-3 against 2.0e-5 on the
ergodic set. Training on the box instead (`SAMPLING_MODE = "exogenous"`, box set to the paper's) produces
a spurious solution: mean Euler error 2.2e-4 on the box, $\lambda$ twice the sparse grid's, and capital that
explodes under simulation (the zero-shock iteration runs off to $10^{20}$). The Euler equations on a box
admit non-transversal paths; the ergodic set is what selects the stable one. That is the sharpest argument
for simulation-based training in the whole course and it is now on the persistent-simulation slide. This is
now stated on the slides and in the session README rather than the
earlier claim that the multiplier is "positive when $k$ is high".

`05_03` was rewritten: its four links pointed into a directory that does not exist, its Task 1 used
$\delta = 0.025$ and $A = 1$ for "the 2-country IRBC model", its Task 2 used invented loss magnitudes
that contradict the real logs (the resource term is the smallest, not the largest), and its Task 3
"measured" a 2.5x speedup that was the ratio of two synthetic decay constants. It now uses the lecture's
calibration, the residual magnitudes from `05_02`'s stored log, and one real re-weighted smoke run.

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

**Session 3 pass, the two engineering decks and their toy codes.** The 03b deck and its notebook told
opposite stories: the deck's results table (ReLoBRaLo best at 0.53) matched no stored output, while
the stored `03_03` run had ReLoBRaLo indistinguishable from equal weighting and non-dimensionalisation
a hundred times better; the two figure captions described weight and loss behaviour the figures do not
show, and the temperature figure was an old bar chart the notebook itself had replaced. The 03a deck
referenced a 10-D notebook that does not exist, quoted an invented depth/width bar chart, and showed a
results figure from a different run than the stored one. On the code side, `03_02` selected and
reported on the same 2,000 points, retrained every successive-halving survivor from scratch, capped
the learning rate at $10^{-2}$ where `03_01` had found the optimum, and had a cache cell that raised
`TypeError` whenever `RUN_MODE` differed from the cached run (the in-class smoke setting), or, had it
not, would have overwritten the teaching cache with smoke trials. `03_03`'s argument that the softmax
ceiling $e^{1/T}$ limits ReLoBRaLo was wrong for the run it described: with $\alpha=\rho=0.999$ and
one update per epoch, the smoothing caps the weights at a few percent of movement whatever $T$ is.
Both notebooks were rebuilt. `03_02` now has a train / validation / test split, continuation-based
successive halving with an exact 504-epoch budget against 1,500, three seeds, per-preset caches, and a
final section that runs the same random search on the stochastic Brock–Mirman DEQN of `02_02` with
the Euler error as the score (best trial $2.4\cdot10^{-4}$ against $2.1\cdot10^{-3}$ for the `02_02` default and $7.9\cdot10^{-3}$ for the worst draw). `03_03` records the gradient norm each weighted
component sends to the shared parameters, runs ReLoBRaLo per epoch and per optimizer step, and closes
on the labour model of `02_04`, where the gap between the two first-order conditions is $1.2\cdot10^{5}$ in gradient norm
at initialisation and gone by episode 300: transient, unlike the Genz gap, which is in the units. The
decks now carry the measured tables, a frame on natural units tied to what `05_01`/`05_02` code, a
frame each on the DEQN results, and the `03_01` table on when random search actually beats grid
search. Frame counts unchanged (27 and 29). Both decks' figures are written by the stored teaching
runs, so every number on a results frame is in a stored output cell.

**Sessions 6 and 7 pass, surrogates, Gaussian processes and SMM.** Both decks were leftovers of a
90-minute lecture: the six-part roadmap, objectives about Sobol' indices and the carbon tax, a
"three questions" table with two cut columns, a notation frame, and cross-references to parts that
no longer existed; `07a` opened at Part II and spent four frames on the asymptotic sandwich and
Hall–Inoue pseudo-true parameters; `07b` repeated `07a` with a different colour theme and frames on
a BoTorch acquisition and a GP-over-moments layer that the notebooks no longer contained. The
primer notebook trained a 200k-parameter network on Black–Scholes and its own table showed the
surrogate losing to numpy. The SMM notebooks generated their "data" from the surrogate under the
same shocks as every candidate, so the criterion was identically zero and the estimate exact by
construction; nothing validated the surrogate against a solution of the model. Rebuilt around one
shared reference solver, `day2/code/brock_mirman_reference.py` (endogenous grid method, cubic splines,
Euler errors below 1e-6 at every corner of the parameter box, one to two seconds per solve): the
primer fits a GP and a network to the same labels of a Brock–Mirman quantity of interest and
measures both as the label budget grows; the GP notebook is the old one trimmed to its sound parts
plus the two-input case; the SMM notebooks take their data from the reference solution, validate the
pseudo-state policy network against it at four and five parameter values, simulate under common
random numbers, minimize on the fly, and lay the surrogate's criterion over the reference solver's.
Tuning notes: the policy network needs the log of capital as an input, a capital box wide enough for
the ergodic set at ρ = 0.99 (which spans a factor of ten), width 128 and about 12,000 steps; sampling
log z within each candidate's own ergodic range made things worse. The near-unit-root end ρ = 0.99 is
the hardest and is reported as measured: mean consumption error $1.1\cdot10^{-3}$ and max $2.1\cdot10^{-2}$ at ρ = 0.99 in `07_01`, against $2.1\cdot10^{-4}$ mean at the best ρ. Decks: 06 has 29 frames, 07 has
24 (from 39 and 21 + 21); `07b` is gone, its finger exercise replaced by the AR(1)-variance
one in the deck.

## Compute

No notebook needs a GPU. Measured on the laptop CPU: Session 4, `04_00` 69 s, `04_01` 11 min at the teaching preset
and 2.5 min at smoke, `04_04` 3.5 min, `04_02` 49 min (not taught); Session 5, `05_01` 3 min at the
teaching preset and under a minute at smoke, `05_02` 3 min, `05_01` with ten countries 8 min; Session 3, `03_01` 10 min, `03_02` 29 min from scratch and 2 min from
its committed caches, `03_03` 12 min, all at the teaching preset. Sessions 6 and 7: `06_01` 6 min (220 reference solves at
about 1.7 s each), `06_02` 30 s, `07_01` 3 min, `07_02` 8 min (the GP route adds 24 reference solves). The stored outputs are the teaching runs,
so nobody has to reproduce them; in class students run `"smoke"`.

## Open items

* Confirm room and local contact details with the Padova organizers.
* Decide whether to set the DEQN exercise blanks (`02_03`) as an assessed take-home.
