### Exercise 2 - Environments, Documenting, and Sharing your Project (65 mins)

#### Snapshot it (25 mins)
Code that runs fine today can quietly stop working in six months, or on someone else's laptop right now — not because the code changed, but because the packages underneath it did. Fixing this means writing down exactly what your environment looked like when everything worked.

1. If you don't already have one, create a conda environment for your project and install what you need.
2. Export it: `conda env export > environment.yml` (or `pip freeze > requirements.txt` if you're not using conda).
3. Commit the environment file to your repo.

**Partner check**: swap repos with someone nearby. Can they clone your repo, rebuild your environment from the file you just committed, and get your code running — without asking you anything? If not, what's missing?

This is the bridge from everything you've done in W1 and W2 to next week's HPC session — you'll rebuild this exact environment on the cluster.

**Menti check**: who does capturing your environment actually help? [Link]

#### README + Repo→DOI (40 mins)

**Write a README that lets someone rerun your project cold.** At minimum it should answer:
- what does this project do, and on what data?
- how do you set up the environment? (point to `environment.yml`)
- what order do you run things in, to get from raw data to the results?
- where does the raw data actually live? (link to RDSS or wherever you put it)

Keep it short — a few minutes' read, not a manual.

**Publish a real, citable version of your project:**
1. Make sure your README, `.gitignore`, and environment file are all committed and pushed.
2. If you don't already have one, create an [ORCID](https://orcid.org) — most of you should have this already from the pre-session setup.
3. Go to [zenodo.org](https://zenodo.org) and link your GitHub account (a quick one-minute authorisation, not a full separate signup).
4. Find your repo in the Zenodo GitHub integration and switch it on.
5. Back on GitHub, create a new **Release** (tag it, e.g. `v1.0`) — this triggers Zenodo to archive it and mint a DOI.
6. Copy the DOI badge markdown Zenodo gives you and add it to the top of your README.

**Before you publish**: this is a real, public, permanent-ish record. Zenodo does let you delete a record within 30 days of publishing — but the DOI itself gets indexed straight away, so "deleted" doesn't undo the fact that it existed and was citable. That's not a reason to panic, it's exactly the kind of decision you'll be making with real research outputs — publishing a DOI is a commitment, even with a nominal undo button.

If your project has a real dataset that should live somewhere more permanent than Zenodo's storage (large data, sensitive data, or data with a natural disciplinary home), have a quick look at [fairsharing.org](https://fairsharing.org) or [re3data.org](https://re3data.org) to see where it would actually belong — you don't need to upload anywhere today, just get a sense of what exists.

**Menti check**: who does documentation, metadata, and a real DOI actually help? [Link]

#### Summary
Your project is now structured, environment-captured, documented, and has a real, citable DOI attached to it. Go check your rerun-test sticky note from this morning — how many of those failure points would still happen to someone opening this repo today?
