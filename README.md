# Readme2

Developers like building things and dislike writing about them. Readme2 interviews you
about your project the way a magazine or a TV channel would, then writes the article
from your own answers. The goal is a README 2.0: the story, the choices and the numbers
behind code that would otherwise stay hidden on GitHub.

Status: **V1**, a written interview that produces one technical article.

## How it works

The interview follows the practices of professional interviewers (oral history,
journalism, qualitative research), in eight phases:

1. **Framing**: angle, audience, sources.
2. **Research**: the skill reads your repo, docs and notes before asking anything, and
   builds a dated timeline with the gaps no document records.
3. **Pre-interview**: what matters to you, what is off limits, what stays private.
4. **Interview guide**: a plan you validate before the interview starts.
5. **Interview**: one question at a time, anchored on real dates and facts.
6. **Debrief**: what was learned, how reliable it is, what it changes.
7. **Material bank**: exact quotes, stories, numbers. You validate each one.
8. **Article**: written only from the validated bank, then a style pass and an
   automatic check (no unresolved gap, every quote found word for word in the
   transcript).

Four gates stop the process until you say go: framing, guide, bank, final article.

## What it never does

- Invent a fact, a number, a date or a quote. A gap stays marked `[?]`.
- Put a reason in your mouth that you did not give.
- Raise a topic you declined.
- Publish anything you have not approved.

## Install

**Claude Code**: copy the skill into your personal skills folder.

```bash
git clone https://github.com/malikkaraoui/Readme2.git
mkdir -p ~/.claude/skills
cp -R Readme2/skills/readme2-interview ~/.claude/skills/
```

**Claude app (Cowork)**: zip the `skills/readme2-interview` folder, then upload and
enable it in your claude.ai skill settings.

## Use

In a session opened on your project, say:

> Interview me about this project.

The skill creates `interviews/<slug>/` in your project and keeps every step there, so
an interview can stop and resume across sessions.

## Roadmap

- **V1** (now): written interview → one article.
- **V2**: audio interview, article series, social posts, podcast in your own
  synthesised voice, motion video.
- **V3**: a public hub where investors, project leads and developers discover projects
  through their README 2.0.

## Sources

The method and its sources are in
[`skills/readme2-interview/references/`](skills/readme2-interview/references/).

## License

MIT
