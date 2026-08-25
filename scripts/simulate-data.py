#!/usr/bin/env python3
"""
Generate the synthetic dataset for the UCL Biosciences Computational
Training course.

One dataset: activity counts for a colony of naked mole-rats.

    rows    = animals
    columns = successive observation sessions
    values  = activity count for that animal in that session

No header row, no text columns, one measurement type throughout, so

    numpy.loadtxt(fname='molerat_activity_v1.csv', delimiter=',')

works with no further arguments.

Row layout
----------
The first BREEDERS rows are breeding animals. Everything after that is a
non-breeder. Nothing in the file says so - participants are told the
ordering and compare the two blocks themselves:

    data[:100].mean(axis=0)     vs     data[100:].mean(axis=0)

Breeders are much less active, so the difference is easy to see.

What the clustering exercise is for
-----------------------------------
The non-breeders are not one thing. Some are workers, who are highly
active, and some are soldiers, who sit in between breeders and workers.
They are shuffled together in the file, and nothing marks which is which.
Clustering the animals by their activity recovers three groups without
being told there are three, or what they are.

The separation is deliberately clear enough that k-means on the raw counts
finds it. Run with --labels to write a companion file of true group names
for checking the answer afterwards.

The reference colony
--------------------
    molerat_reference_v1.csv

A second, separate colony that was observed intensively enough for every
animal's role to be known. It has a header row and a "role" column, then
one column per session. Equal numbers of each role, because the animals
were picked deliberately rather than sampled from a colony.

This is the training set. A model is fitted here, on known roles, and then
used to predict roles in the main colony, where nothing is labelled. That
is a real workflow, and it keeps the training labels independent of the
data being predicted - unlike clustering the main colony and then
predicting its own cluster labels, which is circular.

The reference colony was observed under slightly different conditions, so
its counts run a little higher throughout. Models that lean on absolute
activity levels transfer worse than models that use the relative shape.

Why a linear model struggles
----------------------------
"Is this animal a soldier?" cannot be answered by a straight line.
Soldiers sit between breeders and workers, so isolating them means cutting
the middle out of a range, and a single threshold cannot do it. Logistic
regression scores below chance; a random forest is near perfect; and
per-animal mean activity alone scores exactly 0.500.

The classes have to be balanced for this to show. In a whole colony there
are six times as many workers as breeders, so "high activity means not a
soldier" is right often enough that a logistic regression reaches ~0.84
and the contrast disappears. The reference colony is balanced by design,
which is one reason to train on it.

Two versions:
    v1  the dataset participants build their notebook against
    v2  the same study run again. Same shape, same row layout, different
        values. A notebook written against v1 should run on v2 unchanged
        and produce visibly different figures.

Nothing here is biologically meaningful. It is shaped to be recognisable,
not to be true.

Where the files go
------------------
By default the files are written into the workshop folders that use them,
found by glob so that renaming a workshop does not break this script:

    workshops/W1*/data/    activity matrices
    workshops/W4*/data/    activity matrices, reference colony, labels

W1 gets the activity matrices to plot. W4 is the AI session, so it gets
the reference colony to train on and the activity matrices to predict.

Use --outdir to write everything to one folder instead, for testing.

Usage:
    python simulate-data.py
    python simulate-data.py --outdir /tmp/check
    python simulate-data.py --animals 500 --sessions 40
    python simulate-data.py --animals 5000000        # large file for HPC
"""

import argparse
from pathlib import Path

import numpy as np

# --------------------------------------------------------------------------
# Study design
# --------------------------------------------------------------------------

ANIMALS = 300
SESSIONS = 30

# Proportions of the colony. Breeders always occupy the first rows;
# workers and soldiers are shuffled together after them.
BREEDER_FRAC = 0.33
SOLDIER_FRAC = 0.33
# workers take the remainder

# Mean activity counts per session for each group. These set how far apart
# the clusters sit - the gaps are what k-means finds.
LEVELS = {"breeder": 5.0, "soldier": 12.0, "worker": 22.0}

# Animal-to-animal variation. Increased from 0.12 to 0.35 so that soldiers
# and workers overlap enough to make the multiclass classification problem
# genuinely hard while breeders remain clearly separable.
INDIVIDUAL_SPREAD = 0.35
SESSION_SPREAD = 0.08       # session-to-session variation in conditions

V2_SHIFT = 1.15             # v2 runs a little busier throughout

# The reference colony: equal numbers of each role, all known.
# Which workshop folders get which files. The globs mean a workshop can be
# renamed without touching this script, as long as the W-number survives.
DESTINATIONS = [
    ("workshops/W1*", {"activity"}),
    ("workshops/W4*", {"activity", "reference", "labels"}),
]

REFERENCE_PER_ROLE = 100
REFERENCE_SHIFT = 1.10      # observed under slightly different conditions


def build(animals, sessions, version, seed):
    rng = np.random.default_rng(seed)

    n_breeder = int(round(animals * BREEDER_FRAC))
    n_soldier = int(round(animals * SOLDIER_FRAC))
    n_worker = animals - n_breeder - n_soldier

    rest = np.array(["soldier"] * n_soldier + ["worker"] * n_worker)
    rng.shuffle(rest)
    labels = np.concatenate([np.array(["breeder"] * n_breeder), rest])

    level = np.array([LEVELS[g] for g in labels], dtype=float)
    level = level * rng.lognormal(0.0, INDIVIDUAL_SPREAD, animals)

    session_factor = rng.lognormal(0.0, SESSION_SPREAD, sessions)

    lam = np.outer(level, session_factor)
    if version == 2:
        lam = lam * V2_SHIFT

    return rng.poisson(lam), labels


def build_reference(sessions, version, seed):
    rng = np.random.default_rng(seed + 777)

    roles = np.array(sorted(LEVELS) * REFERENCE_PER_ROLE)
    rng.shuffle(roles)

    level = np.array([LEVELS[g] for g in roles], dtype=float)
    level = level * rng.lognormal(0.0, INDIVIDUAL_SPREAD, len(roles))

    session_factor = rng.lognormal(0.0, SESSION_SPREAD, sessions)

    lam = np.outer(level, session_factor) * REFERENCE_SHIFT
    if version == 2:
        lam = lam * V2_SHIFT

    return rng.poisson(lam), roles


def size_label(n):
    if n >= 1_000_000 and n % 1_000_000 == 0:
        return f"{n // 1_000_000}m"
    if n >= 1000 and n % 1000 == 0:
        return f"{n // 1000}k"
    return str(n)


def resolve_destinations(outdir):
    if outdir is not None:
        return [(Path(outdir), {"activity", "reference", "labels"})]

    root = Path(__file__).resolve().parent.parent
    found = []
    for pattern, wants in DESTINATIONS:
        matches = sorted(d for d in root.glob(pattern) if d.is_dir())
        if not matches:
            print(f"warning: nothing matched {pattern} under {root}")
        for m in matches:
            found.append((m / "data", wants))
    return found


README_TEXT = """\
# Naked mole-rat activity data

## Overview

Activity counts recorded from a captive naked mole-rat colony across a series of observation sessions. Each animal was observed independently in each session and the number of activity events recorded.

This is a synthetic dataset generated for the UCL Biosciences Computational Training course. It is shaped to be biologically recognisable but is not derived from real observations.

## Files

| File | Description |
|---|---|
| `molerat_activity_v1.csv` | Activity matrix, version 1 |
| `molerat_activity_v2.csv` | Activity matrix, version 2 (same colony, second study) |
| `molerat_labels_v1.csv` | Group labels for version 1 (answer key) |
| `molerat_labels_v2.csv` | Group labels for version 2 (answer key) |
| `molerat_reference_v1.csv` | Reference colony with known roles, version 1 |
| `molerat_reference_v2.csv` | Reference colony with known roles, version 2 |

## Activity matrices (`molerat_activity_v*.csv`)

- **Rows:** individual animals ({animals} per file)
- **Columns:** observation sessions ({sessions} per file)
- **Values:** integer activity counts
- **No header row**
- **Delimiter:** comma

The first {breeders} rows are breeding animals (breeders). The remaining rows are non-breeders (soldiers and workers), shuffled together with no indication of which is which.

```python
import numpy as np
activity = np.loadtxt('molerat_activity_v1.csv', delimiter=',')
breeders     = activity[:{breeders}]
non_breeders = activity[{breeders}:]
```

## Label files (`molerat_labels_v*.csv`)

- **Rows:** one per animal, matching the row order of the activity matrix
- **Column 1:** binary label — `breeder` or `nonbreeder`
- **Column 2:** full label — `breeder`, `soldier`, or `worker`
- **No header row**
- **Delimiter:** comma

```python
labels = np.loadtxt('molerat_labels_v1.csv', dtype=str, delimiter=',')
binary = labels[:, 0]   # breeder / nonbreeder
multi  = labels[:, 1]   # breeder / soldier / worker
```

## Reference colony (`molerat_reference_v*.csv`)

A separate colony in which every animal's role was known from the outset. Observed under slightly different conditions, so activity counts run a little higher overall.

- **Header row:** `role, s01, s02, ..., s{sessions:02d}`
- **Column 1:** role (`breeder`, `soldier`, or `worker`)
- **Remaining columns:** activity counts per session
- **Rows:** {reference} animals, equal numbers of each role

```python
data = np.loadtxt('molerat_reference_v1.csv', delimiter=',', dtype=str, skiprows=1)
roles    = data[:, 0]
activity = data[:, 1:].astype(int)
```

## Colony roles

| Role | Mean activity (counts/session) | Description |
|---|---|---|
| Breeder | ~5 | Reproductive animals; low activity, rarely leave the nest |
| Soldier | ~12 | Colony defence; intermediate activity |
| Worker | ~22 | Foraging and tunnel maintenance; highest activity |

Activity levels overlap between soldiers and workers. Breeders are clearly separated from both.

## Versions

Version 1 and version 2 represent two independent studies of the same colony type. They have identical structure and row layout but different values. A script written against v1 should run on v2 without modification.

## Generation

Files were generated by `scripts/simulate-data.py` in the course repository. Re-running the script will regenerate all files deterministically from fixed random seeds.

## Licence

Generated for educational use. No restrictions on reuse.
"""


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--outdir", default=None,
                    help="write everything here instead of the workshop "
                         "folders")
    ap.add_argument("--animals", type=int, default=ANIMALS)
    ap.add_argument("--sessions", type=int, default=SESSIONS)
    args = ap.parse_args()

    destinations = resolve_destinations(args.outdir)
    if not destinations:
        raise SystemExit("no destination folders found - nothing written")

    tag = "" if args.animals == ANIMALS else f"_{size_label(args.animals)}"

    n_breeders = int(round(args.animals * BREEDER_FRAC))
    readme = README_TEXT.format(
        animals=args.animals,
        sessions=args.sessions,
        breeders=n_breeders,
        reference=REFERENCE_PER_ROLE * len(LEVELS),
    )
    for dest, _ in destinations:
        dest.mkdir(parents=True, exist_ok=True)
        f = dest / "README.md"
        f.write_text(readme)
        print(f"{f}  data description")

    for version in (1, 2):
        seed = 100 + version
        activity, labels = build(args.animals, args.sessions, version, seed)
        reference, roles = build_reference(args.sessions, version, seed)

        header = "role," + ",".join(f"s{i + 1:02d}"
                                    for i in range(args.sessions))

        for dest, wants in destinations:
            dest.mkdir(parents=True, exist_ok=True)

            if "activity" in wants:
                f = dest / f"molerat_activity_v{version}{tag}.csv"
                np.savetxt(f, activity, delimiter=",", fmt="%d")
                print(f"{f}  {activity.shape[0]} animals x "
                      f"{activity.shape[1]} sessions")

            if "reference" in wants:
                f = dest / f"molerat_reference_v{version}.csv"
                with open(f, "w") as fh:
                    fh.write(header + "\n")
                    for role, row in zip(roles, reference):
                        fh.write(role + "," +
                                 ",".join(str(v) for v in row) + "\n")
                print(f"{f}  {len(roles)} animals with known roles")

            if "labels" in wants:
                f = dest / f"molerat_labels_v{version}{tag}.csv"
                binary = np.where(labels == "breeder", "breeder", "nonbreeder")
                two_col = np.column_stack([binary, labels])
                np.savetxt(f, two_col, fmt="%s", delimiter=",")
                print(f"{f}  {len(labels)} labels (answer key)")


if __name__ == "__main__":
    main()