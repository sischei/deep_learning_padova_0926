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

414 frames across 540 minutes, about 1.30 minutes per frame overall, before hands-on time.

| Session | Frames | Minutes | Pace |
|---|---:|---:|---|
| 1 Intro to DL | 57 | 90 | 1.58 comfortable |
| 2 DEQNs | 54 | 75 | 1.39 comfortable |
| 3 NAS + loss balancing | 56 | 55 | **0.98 tightest** |
| 4 OLG | 46 | 60 | 1.30 comfortable |
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

**On the OLG session.** It was reviewed line by line because OLG is Padova's research focus. The
mathematics on the slides was right, but the 56-cohort notebook's policy head kept capital saving
bounded away from zero (at 0.0045) and the collateral slack at 8% of it, so neither constraint could
ever bind and both multipliers were trained to zero, the KKT machinery was decorative. The head is
now documented, and §6 of `04_02` measures the binding fraction by age:
with the default head they are zero by construction. Two zero-reachable heads were tried at the teaching preset: an uncapped softplus (capital and bonds run off to infinity after twenty segments) and a capped sigmoid (the policy collapses onto the corners of the head, most cohorts at the cap and the young at zero, with a collateral multiplier of 15). Neither trains without a longer schedule or a smaller learning rate, so the stable bounded-exponential head is the default and the sigmoid is kept as `CONSTRAINT_HEAD = "bounded_sigmoid"` for experimentation. The deck says on III.9 and III.12 that the constraints are slack with the default head. The deck gained a two-period Diamond warm-up (`04_00`), the Euler and
closed-form derivations, an explicit sequence-to-recursive slide, and real teaching-run figures in
place of hand-drawn schematics. The exercise's Task 2 now simulates the model's own ergodic prices
(gross $r \approx 0.69$) instead of assuming $r = 0.15$. IRBC gave up five frames (three code
listings shown live anyway, two merged motivation frames) to make room.

**On the session order.** Architecture search and loss balancing come *before* the two large
applications on purpose: IRBC's country-by-country Euler residuals and the cohort-stacked OLG system
are exactly the multi-component losses that need balancing, so teaching the remedy first means both
applications land on prepared ground. IRBC closes the day as the scaling finale.

## Compute

Notebooks needing a GPU (demo in class, `RUN_MODE = "smoke"` for students on laptops):

* `05_01`, `05_02`, IRBC
* `04_02`, `04_05`, the 56-cohort OLG benchmark
* the optional Aiyagari notebook, not taught

Everything else runs on a laptop CPU in a few minutes.

## Open items

* Confirm room and local contact details with the Padova organizers.
* Decide whether to set the DEQN exercise blanks (`02_03`) as an assessed take-home.
