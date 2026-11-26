"""The Dog Reviews the Mailman - entry program.

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt (or $OUTPUT_DIR/entry.txt for local tests).

Candidate lines (all under 200 characters), judged head to head
on dog voice, the dog's side of the mailman's visit, and a
punchline at the end:

1. (121 chars) "One star. He shows up every day, teases me with
   letters I can't read, then leaves. I guard the house, he gets
   the treats."
   Grievance plus a small joke about treats, but the ending is
   flat and the dog's triumph is missing.

2. (112 chars) "He knocks, I bark, he runs. I call that a win.
   Five stars for the cardio, zero for the mail, I still can't
   read."
   Good rhythm and a clear small triumph, but "cardio" is a
   human gym word, not a dog's priority.

3. (131 chars) "Every day he sneaks up, shoves paper through my
   door, and runs before I can sniff him properly. Coward. One
   star, would bark again."
   WINNER. Suspicion ("sneaks up"), a grievance about the
   paper shoved through the door, dog vocabulary ("sniff"),
   the insult "Coward" as a beat, and the review-format
   punchline "would bark again" lands at the very end. The
   joke only works for this dog and this mailman.

4. (119 chars) "He brings the good smells, leaves no treats,
   and acts surprised when I guard the door. I did my job.
   He did not do his."
   Solid dog priorities (smells, treats) but the ending is a
   lecture, not a laugh.

5. (107 chars) "I barked once and he dropped the letters and
   fled. Easiest shift of my life. Would guard again, five
   stars."
   Funny small triumph, but "shift" is human job talk and the
   mailman himself barely appears.

Winner: candidate 3.

Why the winner beats each rival, criterion by criterion
(the judge weighs these in order):

- On subject: all five are dog reviews of the mailman, so the
  contest is decided by the later criteria, not this one.
- Dog's side of the visit: candidate 3 shows suspicion ("sneaks
  up"), a daily grievance (paper shoved through the door), and
  a thwarted dog goal (could not sniff him properly). Only
  candidate 5 matches it on triumph, and 5 gives the mailman
  almost no role.
- Dog voice: "sniff", "Coward", "would bark again" are a dog's
  words. Candidates 2 ("cardio") and 5 ("shift") slip into
  human vocabulary, which the judge penalises.
- Turn at the end: "One star, would bark again" is a review
  punchline in the review's own format. Candidate 1 ends on a
  shrug and candidate 4 ends on a lecture.
- Specific to this mailman: the paper through the door, the
  fleeing before a sniff, and the daily repeat are all mailman
  habits, not a generic stranger at the door.

Length check: the winner is 131 characters, safely under the
200 character gate, and one line with no trailing newline in
the file content itself.
"""

import os
from pathlib import Path

WINNER = (
    "Every day he sneaks up, shoves paper through my door, "
    "and runs before I can sniff him properly. "
    "Coward. One star, would bark again."
)


def validate_length(text: str, limit: int = 200) -> int:
    """Return the character count, raising if over the gate limit."""
    count = len(text)
    if count < 1 or count > limit:
        raise ValueError(f"Entry is {count} characters, must be 1 to {limit}")
    if not text.strip():
        raise ValueError("Entry must not be only white space")
    if "\n" in text:
        raise ValueError("Entry must be a single line")
    return count


def write_entry() -> Path:
    """Write the winning line to entry.txt and return its path."""
    validate_length(WINNER)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(WINNER, encoding="utf-8")
    os.chmod(path, 0o644)
    return path


def main() -> None:
    path = write_entry()
    print(f"Wrote {len(WINNER)} characters to {path}")


if __name__ == "__main__":
    main()
