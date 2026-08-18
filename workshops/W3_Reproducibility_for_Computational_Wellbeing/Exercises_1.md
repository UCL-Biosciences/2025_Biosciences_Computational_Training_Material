### Exercise 1 - Rerun Test, Structure Rescue, and What's In The Repo (75 mins)

#### The rerun test (15 mins)
Dig out a project instead you haven't touched in at least 6 months.

Look at the files. Can you find everything you'd need to understand and rerun this project — raw data, metadata, code, documentation, results? Note anything missing.
**Make sure you copy/save/protect and important files**, then if there's code, try to rerun it. Without changing anything first, see if you can get from raw data to a known output or figure.

Log where it breaks, or where you got stuck just trying to find things in step 1.

Some common culprits:

- hard-coded file paths that only exist on your machine
- a package that's a different version now, or missing entirely
- a step you did manually and never wrote down
- raw data that's been moved, renamed, or was never saved separately at all
- no idea what half the files even are, six months on

Make a note of something that broke. At the end of the session, we'll look at everyone's problems and see if we have addressed any of them.

#### Structure rescue (25 mins)
A predictable structure means you (or anyone else) can open an unfamiliar repo and know where to look, without reading every file. A reasonable minimum:

```
project/
├── data/
│   ├── raw/          # never edited, never overwritten - read only
│   └── processed/     # regenerated from raw + scripts, safe to delete
├── scripts/           # or notebooks/ - the actual analysis
├── results/           # figures, tables - regenerated, safe to delete
├── requirements.txt    # more on this after the break
└── README.md          # more on this later too
```

The key idea: **raw data is read-only**. If a script writes over your raw data, you've lost your ability to rerun anything from scratch. Everything in `processed/` and `results/` should be things you could delete entirely and regenerate by rerunning your scripts.

1. Look at your folder from the first two weeks. Where does it diverge from this?
2. Reorganise it — move files into `data/raw`, `data/processed`, `scripts/`, `results/` as appropriate.
3. Commit the reorganisation with a clear commit message (e.g. `restructure: separate raw/processed/results`).

**Menti check**: who does a clear structure actually help? [Link]

#### What's in the repo? (35 mins)
Not everything belongs in git. Large raw data files bloat your repository and slow down every clone, forever — git never forgets, even if you delete the file later.

**Sort the following into "commit to git", "add to `.gitignore`", or "store elsewhere entirely":**
- your analysis scripts/notebooks
- a 2GB raw sequencing file
- your `results/` figures
- your environment file
- a spreadsheet of sample metadata
- a folder of cached temporary files

Write a working `.gitignore` for your project based on this sort. (GitHub has good starter templates for Python projects if you want a base to edit.)

**So where does the big raw data actually go?** This is where institutional storage comes in — UCL's Research Data Storage Service (RDSS). You should already have access to a training project we set up in advance.

1. Mount the RDSS training project (or use the web upload client if mounting isn't playing nice — ask if you're stuck).
2. Upload your raw data there instead of committing it to git.
3. **Checkpoint (at the halfway mark)**: by now you should have RDSS mounted and be part-way through uploading. If you're not, flag it now.

This activity is hard time-limited. If you're still stuck when time's up, don't worry — make a note and we'll follow up with you individually after the session, rather than during the workshop.

**Menti check**: who does offloading data to proper storage actually help? [Link]

#### Summary
You now have a repo that's structured sensibly, has a working `.gitignore`, and has its raw data sitting somewhere sensible rather than bloating your git history. None of that touches whether the *code itself* still runs elsewhere, though — that's next, after the break.
