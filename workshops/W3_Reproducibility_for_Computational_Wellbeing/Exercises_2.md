### Exercise 2 - Environments, Documenting, and Sharing your Project (65 mins)

#### Library snapshots using environments (25 mins)
Most projects require a set of code libraries in order to run, which means a project you started on your laptop won't necessarily work on your desktop or on your colleague's computer. And code that runs fine today can quietly stop working in six months — not because the code changed, but because the packages underneath it did. And sometimes, subtle changes as packages are upgraded can have meaningful impacts on your results! So you might have a different set of results and no idea why!

Fixing this means writing down exactly what your environment looked like when everything originally worked.

##### Conda environments
Conda is a system for managing packages. It is a package manager - it has a big archive of packages that you can search for and download. Includes python but also R, CL bioinformatics etc. It is also an environment manager. You can use it to make separate project workspaces called "environments". Using separate environments means you can have different versions of packages for different projects. Is surprisingsly essential when working with python libraries.

So, conda is for 1. installing packages and 2. managing reproducible environments.

**Create an environment**
Open a terminal window in Visual Studio Code.

`conda create -n project-dna pandas=2.3.3`

**Activate it**. To work with an environment, it has to be activated. You can also deactivate it with `conda deactivate`.

`conda activate project-dna`

**Install packages**.
First install a general python package:

`conda install jupyter`

Then look up a package online relevant to your project and install it:

`conda install <YOUR PACKAGE HERE>`

**Take a snapshot**. Export the list of packages in the environment and save it to file:

`conda export --file=requirements-project-dna.yaml`

**Add the file to your github repository**. Make sure your terminal is in the right folder by using `Open Folder` in Visual Studio Code.To add files to repo using the command line:

```
git add requirements-project-dna.yaml # add this to your local repo's "staging area", getting ready to go out on the big stage (aka github)
git commit -m "" # add a message to explain what you are doing
git push # send the changes to your "remote" github repository
```

**Test it** Could we run the workshops from week 1 using this workbook? What do we need to install? Can you make it happen? Stretch goal...

**Partner check**: swap repos with someone nearby. Can they clone your repo, rebuild your environment from the file you just committed, and get your code running — without asking you anything? If not, what's missing?

This is the bridge from everything you've done in W1 and W2 to next week's HPC session — you'll rebuild this exact environment on the cluster.

**Menti check**: who does capturing your environment actually help? [Link]

#### README + Repo→DOI (40 mins)

**Write a README that lets someone rerun your project cold.** At minimum it should answer:
- what does this project do, and on what data?
- how do you set up the environment? (point to requirements file)
- what order do you run things in, to get from raw data to the results?
- where does the raw data actually live? (link to RDSS or wherever you put it)

Keep it short — a few minutes' read, not a manual.

**Publish a real, citable version of your project:**
1. Make sure your README and environment file are all committed and pushed.
2. If you don't already have one, create an [ORCID](https://orcid.org) — most of you should have this already from the pre-session setup.
3. Go to [zenodo.org](https://zenodo.org) and link your GitHub account (a quick one-minute authorisation, not a full separate signup).
4. Find your repo in the Zenodo GitHub integration and switch it on.

**Before you publish**: this is a real, public, permanent-ish record. Zenodo does let you delete a record within 30 days of publishing — but the DOI itself gets indexed straight away, so "deleted" doesn't undo the fact that it existed and was citable. That's not a reason to panic, it's exactly the kind of decision you'll be making with real research outputs — publishing a DOI is a commitment, even with a nominal undo button.
  
5. Back on GitHub, create a new Release and tag it (e.g. `v1.0`) by clicking the tag symbol, to the left of `main` and the branches icon. This triggers Zenodo to archive it and mint a DOI.
6. Copy the DOI badge markdown Zenodo gives you and add it to the top of your README.

#### Publishing real datasets
If your project has a real dataset that should live somewhere more permanent than Zenodo's storage (large data, sensitive data, or data with a natural disciplinary home), have a quick look at [fairsharing.org](https://fairsharing.org) or [re3data.org](https://re3data.org) to see where it would actually belong — you don't need to upload anywhere today, just get a sense of what exists.


**Menti check**: who does documentation, metadata, and a real DOI actually help? [Link]

#### Summary
Your project is now structured, environment-captured, documented, and has a real, citable DOI attached to it. Go check your rerun-test sticky note from this morning — how many of those failure points would still happen to someone opening this repo today?
