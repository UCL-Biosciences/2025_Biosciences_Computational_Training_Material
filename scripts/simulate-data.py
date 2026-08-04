#!/usr/bin/env python3
"""
Generate synthetic teaching datasets for the UCL Biosciences Computational
Training course.

Written by Claude 02 08 26

Run in carpentries environment: https://raw.githubusercontent.com/carpentries/workshop-template/refs/heads/gh-pages/data/carpentries_environment.yml 

Four domains (genomics, imaging, neuro, structural), all sharing a common
schema so that one set of Week 1 materials works for any of them:

    sample_id | group | batch | measure_1 | <8-10 domain columns> | target_a | target_b

Two outcome columns, for the Week 5 contrast:
    target_a  driven by a straightforward additive combination of three
              columns. A logistic regression handles it well.
    target_b  driven by an interaction between two columns (the outcome
              depends on them moving together, not on either level) plus an
              intermediate optimum on a third (best at mid-range, worse at
              both extremes). No single column separates the classes, so
              t-tests and correlations find nothing and a main-effects
              logistic regression scores ~0.50. A tree-based model finds it
              without being told the structure. Adding the right interaction
              and quadratic terms to the regression also recovers it - the
              point is that ML did not need to be told.

Two versions per domain:
    v1  the dataset participants build their notebook against
    v2  the same experiment run again: identical schema, same groups, same
        batch labels, same column order. New sample IDs, rows in a different
        order, and different values. A notebook written against v1 should
        run on v2 unchanged and produce visibly different figures.

The data is clean. No missing values, no mixed-type columns, no duplicate
IDs. Every numeric column loads as numeric.

Nothing here is biologically meaningful. It is shaped to be recognisable,
not to be true.

Usage:
    python make_teaching_data.py                     # 1k and 10k, all domains
    python make_teaching_data.py --domain neuro      # just one domain
    python make_teaching_data.py --rows 50000000     # one large file per domain/version
    python make_teaching_data.py --rows 1000 --rows 10000 --rows 50000000
"""

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

# --------------------------------------------------------------------------
# Shared schema - identical across all four domains and both versions
# --------------------------------------------------------------------------

ID_COL = "sample_id"
GROUP_COL = "group"
BATCH_COL = "batch"
DEMO_COL = "measure_1"          # generic column, same name in every domain
TARGET_A = "target_a"
TARGET_B = "target_b"

GROUPS = ["Control", "TreatmentA", "TreatmentB"]
BATCHES = ["B01", "B02", "B03"]

TARGET_AUC_SCALE = 1.6          # target_a: tuned so a simple model lands ~0.8 AUC
INTERACTION_W = 2.2             # target_b: strength of the two-column interaction
OPTIMUM_W = 1.9                 # target_b: strength of the intermediate optimum
V2_SHIFT = 0.45                 # how far v2 moves, in SDs; bigger = more
                                # visibly different figures


# --------------------------------------------------------------------------
# Domain definitions
#
# Each column is (distribution, params, decimals).
#   normal    : (mean, sd)
#   lognormal : (mu, sigma)        -> right-skewed positive values
#   nbinom    : (mean, dispersion) -> overdispersed counts
#   poisson   : (mean,)
#   beta      : (a, b, scale)
#
# "signal"       columns driving target_a, with weights
# "group_effect" columns whose mean differs between treatment groups
# "interaction"  the two columns whose concordance drives target_b
# "optimum"      the column with an intermediate optimum, driving target_b
#
# interaction/optimum deliberately use columns that do NOT drive target_a,
# so the two outcomes are independent structures.
# --------------------------------------------------------------------------

DOMAINS = {
    "genomics": {
        "unit": "sample",
        "prefix": "GEN",
        "columns": {
            "tx_count_total":          ("nbinom",    (1_800_000, 0.3), 0),
            "genes_detected":          ("normal",    (14500, 2200), 0),
            "mito_fraction":           ("beta",      (2, 40, 1.0), 4),
            "ribo_fraction":           ("beta",      (5, 30, 1.0), 4),
            "mean_gc_percent":         ("normal",    (46.5, 2.1), 2),
            "duplication_rate":        ("beta",      (3, 12, 1.0), 4),
            "median_tx_length":        ("lognormal", (7.4, 0.35), 0),
            "counts_gene_of_interest": ("nbinom",    (450, 0.5), 0),
        },
        "signal": {"mito_fraction": -1.0, "genes_detected": 0.9,
                   "counts_gene_of_interest": 1.1},
        "group_effect": {"counts_gene_of_interest": 0.8, "genes_detected": 0.4},
        "interaction": ("ribo_fraction", "duplication_rate"),
        "optimum": "mean_gc_percent",
    },

    "imaging": {
        "unit": "field_of_view",
        "prefix": "IMG",
        "columns": {
            "nuclei_count":        ("poisson",   (240,), 0),
            "mean_nuclear_area":   ("normal",    (185.0, 34.0), 2),
            "mean_cell_area":      ("normal",    (720.0, 160.0), 2),
            "mean_intensity_dapi": ("normal",    (1420.0, 260.0), 1),
            "mean_intensity_gfp":  ("lognormal", (6.2, 0.55), 1),
            "nuclear_circularity": ("beta",      (12, 3, 1.0), 4),
            "fraction_in_focus":   ("beta",      (18, 2, 1.0), 4),
            "background_sd":       ("lognormal", (3.1, 0.4), 2),
        },
        "signal": {"mean_intensity_gfp": 1.2, "nuclei_count": 0.7,
                   "nuclear_circularity": -0.8},
        "group_effect": {"mean_intensity_gfp": 0.9, "nuclei_count": 0.5},
        "interaction": ("mean_intensity_dapi", "mean_cell_area"),
        "optimum": "mean_nuclear_area",
    },

    "neuro": {
        "unit": "cell",
        "prefix": "NEU",
        "columns": {
            "resting_potential_mv":  ("normal",    (-65.0, 5.5), 2),
            "input_resistance_mohm": ("lognormal", (5.2, 0.45), 1),
            "membrane_tau_ms":       ("lognormal", (2.6, 0.4), 2),
            "rheobase_pa":           ("normal",    (110.0, 38.0), 1),
            "ap_threshold_mv":       ("normal",    (-42.0, 4.2), 2),
            "ap_half_width_ms":      ("lognormal", (0.05, 0.3), 3),
            "max_firing_rate_hz":    ("normal",    (48.0, 14.0), 1),
            "spike_count":           ("poisson",   (86,), 0),
            "adaptation_index":      ("beta",      (4, 6, 1.0), 4),
        },
        "signal": {"max_firing_rate_hz": 1.1, "input_resistance_mohm": -0.9,
                   "ap_half_width_ms": 0.8},
        "group_effect": {"max_firing_rate_hz": 0.7, "rheobase_pa": -0.6},
        "interaction": ("membrane_tau_ms", "adaptation_index"),
        "optimum": "resting_potential_mv",
    },

    "structural": {
        "unit": "structure",
        "prefix": "STR",
        "columns": {
            "resolution_ang":       ("lognormal", (0.65, 0.32), 2),
            "r_free":               ("normal",    (0.235, 0.035), 4),
            "chain_length_aa":      ("lognormal", (5.6, 0.6), 0),
            "molecular_weight_kda": ("lognormal", (3.5, 0.6), 2),
            "fraction_helix":       ("beta",      (5, 7, 1.0), 4),
            "fraction_sheet":       ("beta",      (4, 9, 1.0), 4),
            "mean_b_factor":        ("lognormal", (3.5, 0.45), 2),
            "radius_gyration_ang":  ("normal",    (24.5, 6.2), 2),
            "ligand_count":         ("poisson",   (2.4,), 0),
            "isoelectric_point":    ("normal",    (6.9, 1.4), 2),
        },
        "signal": {"resolution_ang": -1.2, "r_free": -1.0,
                   "mean_b_factor": -0.7},
        "group_effect": {"resolution_ang": -0.6, "mean_b_factor": -0.5},
        "interaction": ("fraction_helix", "fraction_sheet"),
        "optimum": "isoelectric_point",
    },
}


# --------------------------------------------------------------------------
# Samplers
# --------------------------------------------------------------------------

def sample_column(rng, dist, params, n):
    """Draw n values from the named distribution."""
    if dist == "normal":
        mean, sd = params
        return rng.normal(mean, sd, n)
    if dist == "lognormal":
        mu, sigma = params
        return rng.lognormal(mu, sigma, n)
    if dist == "poisson":
        (lam,) = params
        return rng.poisson(lam, n).astype(float)
    if dist == "nbinom":
        # parameterised by mean and dispersion (smaller = more overdispersed)
        mean, disp = params
        r = 1.0 / disp
        p = r / (r + mean)
        return rng.negative_binomial(r, p, n).astype(float)
    if dist == "beta":
        a, b, scale = params
        return rng.beta(a, b, n) * scale
    raise ValueError(f"unknown distribution: {dist}")


def urank(x):
    """
    Rank-transform to a centred, unit-variance scale.

    Used only when building target_b. The domain columns are skewed, counted
    or bounded, and a raw product of two of them would be dominated by a few
    extreme values. Ranking makes the interaction behave the same way in
    every column regardless of its distribution.
    """
    x = np.asarray(x, dtype=float)
    r = np.empty(len(x))
    r[np.argsort(x)] = np.arange(1, len(x) + 1)
    return (r / (len(x) + 1) - 0.5) * 2 * np.sqrt(3)


def zscore(x):
    x = np.asarray(x, dtype=float)
    sd = x.std()
    return (x - x.mean()) / (sd if sd > 0 else 1.0)


# --------------------------------------------------------------------------
# Frame construction
# --------------------------------------------------------------------------

def build_frame(domain, n, version, seed):
    """
    Build one dataset.

    v1 and v2 are identical in schema: same columns, same order, same group
    labels, same batch labels. They differ in sample IDs, row order, and
    values.
    """
    cfg = DOMAINS[domain]
    rng = np.random.default_rng(seed)

    # Sample IDs: same convention, different numbers.
    offset = 0 if version == 1 else 500_000
    ids = [f"{cfg['prefix']}-{i + offset:06d}" for i in range(1, n + 1)]

    group = rng.choice(GROUPS, n)
    batch = rng.choice(BATCHES, n)

    df = pd.DataFrame({ID_COL: ids, GROUP_COL: group, BATCH_COL: batch})

    raw = {}
    for name, (dist, params, dec) in cfg["columns"].items():
        vals = sample_column(rng, dist, params, n)

        # Per-group mean shift, so there is something real to plot.
        if name in cfg["group_effect"]:
            effect = cfg["group_effect"][name]
            spread = np.std(vals)
            for gi, g in enumerate(GROUPS):
                shift = effect * spread * (gi - (len(GROUPS) - 1) / 2)
                vals[group == g] += shift

            # v2 moves the whole column, so regenerated figures visibly change.
            if version == 2:
                vals += V2_SHIFT * spread * effect

        raw[name] = vals

    # target_a: additive, linear. A regression handles this well.
    logit_a = np.zeros(n)
    for name, weight in cfg["signal"].items():
        logit_a += weight * zscore(raw[name])
    logit_a = TARGET_AUC_SCALE * logit_a / np.sqrt(
        sum(w ** 2 for w in cfg["signal"].values())
    )
    target_a = (rng.random(n) < 1.0 / (1.0 + np.exp(-logit_a))).astype(int)

    # target_b: interaction + intermediate optimum. Invisible to t-tests,
    # correlations and a main-effects regression; findable by a tree.
    ia, ib = cfg["interaction"]
    logit_b = (INTERACTION_W * urank(raw[ia]) * urank(raw[ib])
               + OPTIMUM_W * (0.8 - urank(raw[cfg["optimum"]]) ** 2))
    logit_b -= logit_b.mean()
    target_b = (rng.random(n) < 1.0 / (1.0 + np.exp(-logit_b))).astype(int)

    # Generic demo column, same name in every domain.
    df[DEMO_COL] = np.round(rng.normal(100.0, 15.0, n), 2)

    for name, (dist, params, dec) in cfg["columns"].items():
        vals = np.round(raw[name], dec)
        df[name] = vals.astype("int64") if dec == 0 else vals

    df[TARGET_A] = target_a
    df[TARGET_B] = target_b

    # v2 rows arrive in a different order. IDs stay attached to their rows;
    # only the ordering changes.
    if version == 2:
        df = df.iloc[rng.permutation(n)].reset_index(drop=True)

    return df


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------

SEEDS = {"genomics": 11, "imaging": 22, "neuro": 33, "structural": 44}


def size_label(n):
    if n >= 1_000_000 and n % 1_000_000 == 0:
        return f"{n // 1_000_000}m"
    if n >= 1000 and n % 1000 == 0:
        return f"{n // 1000}k"
    return str(n)


def generate(outdir, domains, sizes):
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    written = []

    for domain in domains:
        for version in (1, 2):
            for n in sizes:
                seed = SEEDS[domain] + version * 1000 + n
                df = build_frame(domain, n, version, seed)
                p = outdir / f"{domain}_v{version}_{size_label(n)}.csv"
                df.to_csv(p, index=False)
                written.append(p)

    return written


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--outdir", default="data")
    ap.add_argument("--domain", choices=sorted(DOMAINS), action="append",
                    help="restrict to one or more domains (default: all)")
    ap.add_argument("--rows", type=int, action="append",
                    help="row counts to generate; repeatable "
                         "(default: 1000 and 10000). Use a large value here "
                         "to produce the oversized file for the HPC session.")
    args = ap.parse_args()

    domains = args.domain or sorted(DOMAINS)
    sizes = args.rows or [1000, 10000]

    for p in generate(args.outdir, domains, sizes):
        print(f"{p}  ({p.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
