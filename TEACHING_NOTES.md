# Teaching notes

Internal notes for running the Padova suite. Not part of the student-facing material.

## Where this material came from

Every deck and notebook is drawn from the full-length course. The source decks kept for provenance
live in [`_sources/`](_sources); the tools used to re-cut them are in [`_tools/`](_tools):

* `_tools/section_select.py` — rebuild a shortened deck by keeping a subset of `\section` blocks.
  Dropped sections are left as commented markers, so the result stays diffable against its source.
* `_tools/frame_extract.py` — pull named frames out of a deck by title. Used to build Session 9.
* `_tools/smoke_test.sh` — execute the CPU-light notebooks end to end.

Re-cuts applied:

| Deck | Change |
|---|---|
| `02_DeepEquilibriumNets` | Dropped *Loss Balancing* and *Architecture Search* — these became Session 4, taught from dedicated decks. 77 → 54 frames. |
| `06_Deep_Surrogates_and_GPs` | Dropped *Structural Estimation* (→ Session 7) and *Optimal Carbon Tax* / *Quantify: Uncertainty* (climate; no setup in this course). 75 → 39 frames. |
| `07a_Structural_Estimation_SMM` | The estimation section of the surrogates deck, standing alone. |
| `08_PINNs` | Dropped *Black–Scholes* to self-study. 57 → 53 frames. |
| `09_Continuous_Time_HA` | **New.** 26-frame extract from the two 60-frame continuous-time decks. |
| `10_Wrap_Up` | **New.** Rewritten for a two-day arc; climate-specific slides replaced. |

## Timing

429 frames across 540 minutes — about 1.26 minutes per frame overall, before hands-on time.

| Session | Frames | Minutes | Pace |
|---|---:|---:|---|
| 1 Intro to DL | 57 | 90 | 1.58 comfortable |
| 2 DEQNs | 54 | 75 | 1.39 comfortable |
| 3 IRBC | 55 | 55 | 1.00 tight |
| 4 NAS + loss balancing | 56 | 55 | **0.98 tightest** |
| 5 OLG | 37 | 55 | 1.49 comfortable |
| 6 Surrogates + GPs | 39 | 50 | 1.28 comfortable |
| 7 SMM | 42 | 55 | 1.31 comfortable |
| 8 PINNs | 53 | 55 | 1.04 tight |
| 9 CT-HA + wrap-up | 36 | 50 | 1.39 comfortable |

**Trim order if running long:** the GradNorm comparison in Session 4 → the Bayesian active-learning
demo in Session 6 → the master-equation slide in Session 9.

Sessions 3, 4 and 8 are the ones to watch. Session 4 has the least slack, and it is also the session
where a live demo is most tempting — consider running `04_02` from its cached `nas_results/` rather
than re-searching.

## Compute

Notebooks needing a GPU (demo in class, `RUN_MODE = "smoke"` for students on laptops):

* `03_01`, `03_02` — IRBC
* `05_02`, `05_05` — the 56-cohort OLG benchmark
* `09_02` — continuous-time Aiyagari

Everything else runs on a laptop CPU in a few minutes.

## Open items

* Confirm room and local contact details with the Padova organizers.
* Decide whether to set the DEQN exercise blanks (`02_03`) as an assessed take-home.
