# Output formats

V1 produces one format: the article. Later formats are listed at the end so the bank
collects what they will need.

## Article (V1)

**Input:** `06-bank.md` with `validated: yes`, plus `01-sources.md` for dates and facts.
Nothing else.

**Before writing**, state in two lines at the top of the draft (then delete them):
the angle, and the single thread that carries the article (usually the timeline or one
turning point).

**Structure:** cut to length and arranged in logical order (Paris Review). Choose one:
- *Narrative*: chronological, each section opens on a dated moment from the bank.
- *Problem → solution*: the problem in the interviewee's words, what they tried, what
  worked, the measured result, what they would do differently.

**Rules**
- First person, the interviewee's voice, unless the framing chose a journalist's voice
  (third person with quotes).
- Every fact traces to the bank or the sources. Every quote is exact and appears in
  `04-transcript.md`. When the article language differs from the interview language,
  use the translation validated in the bank and keep the meaning; never paraphrase a
  translated quote further.
- Every reason ("because", "so that") comes from the interviewee.
- No `[?]` left: drop the claim or ask the interviewee before writing.
- Numbers keep their referent and date ("1,275 commits in 44 days", not "a lot").
- An architecture diagram (Mermaid) when the article explains how parts fit together;
  only components the sources confirm.
- Length: as decided in the framing. No length rule is imposed here.
- Then the style pass (`style-pass.md`), then `scripts/check_article.py`.

**Frontmatter of `outputs/article.md`:**
```yaml
---
title: ...
angle: ...
humanizer: pending   # set to done after the style pass
validated_by_interviewee: no
---
```

## Later formats (V2, not built yet)

| Format | What the bank must already hold |
|---|---|
| Article series | several angles or periods, each with its own moment and quotes |
| Social posts | 5 to 7 short, strong quotes (ud-a) |
| Podcast | the strongest moment for a cold open; answers edited first, links written after (The Writer) |
| Motion video | short quotes, numbers, visual moments |
