# Stage 5 — Conclusion

Goal: help the analyst turn findings into an answer with a "so what", already shaped for an SCQA / pyramid deck — without deciding it for them.

## Explore

Read all four previous files and `outputs/report.html`. Draft, privately, a candidate governing thought from the findings the analyst ranked highest.

## Plan: the interview (choices with the analyst's own wording always welcome)

1. **Situation.** "How does the audience see the world today, before this analysis? Proposal: <from 01>."
2. **Complication.** "Which finding is the 'but'? Proposal: F1, because it contradicts the prior belief."
3. **Recommendation.** "What action is realistic for them? Proposal: <…>, sized by <finding>."
4. **Limitation that must be stated.** Proposal from 03/04 (window truncation, missing segment, unexplained delta).
5. **Governing thought in one sentence.** "Proposal: '<…>'. Correct?"

Up to 3 follow-ups. If the analyst disagrees with a proposal, take their version verbatim.

## Code

Only if a number in the conclusion is not yet produced by a script (e.g. "70% of the rise"): add it to `src/04_analysis.py`, run, show. No new analyses here.

## Commit: write `analysis/05_conclusion.md`

```
# 05 Conclusion

## Governing thought
<one sentence, the analyst's words>

## SCQA
- Situation: …
- Complication: …
- Question: <the measurable question, in audience language>
- Answer: <governing thought>

## Pyramid
Answer
├─ Support 1: <claim>  — evidence: F1 (figure, table, check)
├─ Support 2: <claim>  — evidence: F…
└─ Support 3: <claim>  — evidence: F…

## Recommendation
<action, owner, expected effect, what to measure>

## Limitations
- …

## Next problem
<the question this conclusion raises>

## Audit trail
Reproduce: `python run.py`   Commits: ppdac(problem) … ppdac(conclusion)

Approved by analyst: …
```

Regenerate `outputs/report.html`, commit `ppdac(conclusion): …`, then the satisfaction check. When the analyst is satisfied with the conclusion, continue into the final step **in this stage**:

## Final step: build the deck with `/slides`

### Interview first (choices, with "other")
1. **Audience.** Who is in the room, what do they already know, what do they decide? (board / client team / internal / mixed)
2. **Length and setting.** 5 slides in 5 minutes, or 12 in 20? Presented live or read as a document?
3. **Tone.** Persuasive pitch or neutral briefing?
4. **Pushback.** Which support will they challenge most? Which limitation must be on a slide, not in the appendix?
5. **Must-have / must-not.** A figure or list that has to appear; anything that must not (raw tables, a method slide)?

### Storyline before slides
Propose the storyline as **action titles only**, one sentence per slide, the pyramid read top-down: Situation · Complication · Governing thought · Support 1–3 (each a claim with its number) · Recommendation · Limitations · Next question. Iterate on the titles in chat until the analyst approves. Cheap here, expensive later. Do not build slides before the storyline is approved.

### Build
1. Announce: "Building the deck from 05_conclusion.md with /slides: SCQA opening, pyramid body, action titles, one chart per support — a few minutes."
2. Invoke `/slides` with this brief:
   - **Structure**: SCQA in the first 2–3 slides (Situation, Complication, Question/Answer = governing thought). Then the pyramid: one section per support, each with its chart from `outputs/figures/` and the check that backs the number. Then recommendation, limitations, next question. Appendix: method (PPDAC files, `python run.py`, commits).
   - **Action titles**: every slide title is the message as a full sentence ("Homes near the boardwalk sell for 12% less per sqft than comparable inland homes"), never a topic ("Amenity analysis").
   - **One idea per slide**, one chart per slide, source line with script + figure name.
   - Audience, length and tone from the interview above; titles from the approved storyline.
3. Save the deck under `slides/`, commit `ppdac(slides): …`.
4. Iterate: show the outline (titles only) first and ask which slides to change; then apply edits one round at a time ("sharper title on 4", "swap chart on 6 for the map", "cut 8"). Use `AskUserQuestion` for choices where useful. Keep going until the analyst says the deck is good enough.
5. Close: "Deck approved. Files: slides/, analysis/, outputs/report.html. Reproduce with `python run.py`." Then stop.
