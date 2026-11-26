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
"""

import os
from pathlib import Path

WINNER = (
    "Every day he sneaks up, shoves paper through my door, "
    "and runs before I can sniff him properly. "
    "Coward. One star, would bark again."
)


def write_entry() -> Path:
    """Write the winning line to entry.txt and return its path."""
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
