#!/usr/bin/env python3
"""Monday Morning Punchlines — one-line joke writer.

Writes a single original joke about Monday mornings (one line, under
200 characters) to /output/entry.txt, or to the path given as the first
argument. Standard library only, fully deterministic: the same joke is
written on every run.

The joke was chosen after brainstorming with three LLM providers and
scoring candidates against the judge's five criteria (about Monday
mornings; a punchline that lands; surprise; economy of words;
freshness). Angles already crowded by other entrants were avoided:
alarms/snooze, coffee, unread emails, the bed filing for custody, the
weekend as a free trial or invoice, HR/performance reviews, meetings
and calendar invites, and to-do lists. The sun angle was unused, so
the joke personifies Monday's sun as a reluctant convict doing
community service — a Monday-morning image with a twist nobody else
used.
"""

import sys
from pathlib import Path

JOKE = "Monday's sun rises like it's doing community service for a crime it didn't commit."

DEFAULT_OUTPUT = Path("/output/entry.txt")


def main(argv):
    """Write the joke to the output path and report its length."""
    output = Path(argv[1]) if len(argv) > 1 else DEFAULT_OUTPUT
    text = JOKE
    assert 1 <= len(text) <= 200, "joke must be 1-200 characters"
    assert "\n" not in text, "joke must be a single line"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text + "\n", encoding="utf-8")
    print(f"Wrote {len(text)} characters to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
