#!/usr/bin/env python3
"""Final check before an article is shown to the interviewee.

Usage: python3 check_article.py interviews/<slug>

Checks:
  1. outputs/article.md exists
  2. no "[?]" left in the article
  3. every quotation of 4 words or more appears verbatim in 04-transcript.md
  4. 06-bank.md has "validated: yes" in its frontmatter
  5. the article frontmatter has "humanizer: done"

Exit code 0 when everything passes, 1 otherwise. Standard library only.
"""
import re
import sys
from pathlib import Path

# Straight, curly and French quotes. Inline code is ignored.
QUOTE_PATTERNS = [
    r'"([^"\n]+)"',
    r'“([^”\n]+)”',
    r'«\s*([^»\n]+?)\s*»',
]
MIN_QUOTE_WORDS = 4


def frontmatter(text):
    """Return the frontmatter as a dict of simple 'key: value' lines."""
    match = re.match(r"^---\n(.*?)\n---", text, re.S)
    fields = {}
    if not match:
        return fields
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.split("#", 1)[0].strip()
    return fields


def normalise(text):
    """Lowercase, unify apostrophes and collapse whitespace."""
    text = text.replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", text).strip().lower()


def quotes_in(text):
    body = re.sub(r"`[^`]*`", "", text)          # drop inline code
    body = re.sub(r"```.*?```", "", body, flags=re.S)  # drop code blocks
    body = re.sub(r"^---\n.*?\n---", "", body, flags=re.S)  # drop frontmatter
    found = []
    for pattern in QUOTE_PATTERNS:
        found += re.findall(pattern, body)
    return [q for q in found if len(q.split()) >= MIN_QUOTE_WORDS]


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    workspace = Path(sys.argv[1])
    article_path = workspace / "outputs" / "article.md"
    transcript_path = workspace / "04-transcript.md"
    bank_path = workspace / "06-bank.md"

    failures = []
    if not article_path.is_file():
        print(f"FAIL  article not found: {article_path}")
        return 1
    article = article_path.read_text(encoding="utf-8")

    if "[?]" in article:
        failures.append("unresolved [?] left in the article")

    if not transcript_path.is_file():
        failures.append(f"transcript not found: {transcript_path}")
    else:
        transcript = normalise(transcript_path.read_text(encoding="utf-8"))
        for quote in quotes_in(article):
            if normalise(quote) not in transcript:
                failures.append(f'quote not found verbatim in transcript: "{quote}"')

    if not bank_path.is_file():
        failures.append(f"bank not found: {bank_path}")
    elif frontmatter(bank_path.read_text(encoding="utf-8")).get("validated") != "yes":
        failures.append("06-bank.md is not validated by the interviewee (validated: yes)")

    if frontmatter(article).get("humanizer") != "done":
        failures.append("style pass not done (humanizer: done missing)")

    if failures:
        for failure in failures:
            print(f"FAIL  {failure}")
        print(f"\n{len(failures)} problem(s). Fix them before showing the article.")
        return 1
    print("OK  article ready for the interviewee's review")
    return 0


if __name__ == "__main__":
    sys.exit(main())
