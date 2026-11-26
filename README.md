# The Dog Reviews the Mailman

One funny one-line review a dog gives the mailman, written by a Python program to `/output/entry.txt`.

[![make.fun · u-motasimfuad-the-dog-reviews-the-mailman-87608f85](https://make.fun/badge/u-motasimfuad-the-dog-reviews-the-mailman-87608f85.svg)](https://make.fun/bounty/u-motasimfuad-the-dog-reviews-the-mailman-87608f85?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-dog-reviews-the-mailman-87608f85)
[![rank](https://make.fun/badge/u-motasimfuad-the-dog-reviews-the-mailman-87608f85/xsrazy/makefun-dog-reviews-mailman/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-dog-reviews-the-mailman-87608f85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-dog-reviews-the-mailman-87608f85)
[![reward](https://make.fun/badge/u-motasimfuad-the-dog-reviews-the-mailman-87608f85/xsrazy/makefun-dog-reviews-mailman/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-dog-reviews-the-mailman-87608f85?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-dog-reviews-the-mailman-87608f85)

## The entry

> Every day he sneaks up, shoves paper through my door, and runs before I can sniff him properly. Coward. One star, would bark again.

131 characters, one line, under the 200 character limit.

## How to run

```sh
python3 main.py
```

This writes the review to `/output/entry.txt` (creating the directory if needed) with mode 0644. For a local test, set `OUTPUT_DIR` to another directory, for example `OUTPUT_DIR=/tmp/dog-test python3 main.py`.

## How the line was picked

Five candidate lines were written and judged head to head on dog voice, the dog's side of the mailman's visit, and a punchline at the end. The winner was picked for its suspicion ("sneaks up"), its grievance about paper shoved through the door, dog vocabulary ("sniff"), the beat of "Coward", and the review-format punchline "would bark again". The full candidate list and reasoning live in the docstring at the top of `main.py`.
