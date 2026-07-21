### Exercise 2 - Collaborating via GitHub (45-60 mins)
#### Finding a group (5 mins)
Form a group with someone working on a different dataset to yours. Groups can be 2 or more people, as long as there are people working on at least 2 different datasets.

You'll both do every step below — each of you is Repo Owner (for your own repo) and Collaborator (for your partner's repo) at the same time.

#### Giving each other access (5 mins)

Go to your own repo → Settings → Collaborators → Add people. Search your partner's GitHub username and send the invite.
Check your email / GitHub notifications bell for your partner's invite and accept it.

This can take a couple of minutes to come through. While you wait, look at your collaborators repo. Does it look the same as yours? How is it different?

#### Creating a branch on your partner's repo (5 mins)
We're about to send our work and changes to a colleague's repo. If we send it directly, it risks messing up what's already there — especially if the code works and is actually being used or relied on by others. You can't go messing up someone's working pipeline!

It's safer to send our changes to a secure, separate working copy first, before anything gets added to the main version. So we make a working copy — called a branch — of all the contents in the repo and send our changes there instead of straight to the "main" branch. The repo owner can then review the changes and decide whether to accept them or not, without the main content being at risk.

1. On your partner's repo page, click the branch dropdown (usually says `main`) → type a new branch name, e.g. `<your-name>-data` → `Create branch`
2. Make sure the branch selector now shows your new branch, not main

#### Adding your files (10 mins)
Still on your partner's repo, on your new branch:
1. Click `Add file` → `Upload files`. `Add file` is to the left of the big green `Code` button and sometimes minimises to a `+` symbol
2. Drag in your notebook, dataset, and output files from last week
3. Scroll down, add a short commit message, confirm you're committing to your branch (not main), click Commit changes

#### Opening and merging the Pull Request (15 mins)

We've made our changes safely on a separate branch — now we want to bring them into main. But we shouldn't just merge them in blindly; the repo owner hasn't actually seen what's being added yet, and main is the version other people trust and rely on.

It's safer to have a formal review step before anything joins main — a chance for the repo owner to look over exactly what's changed and confirm it's good to bring in. This is called a Pull Request (PR): a formal request to merge your branch into main, which sits open for review until someone with permission accepts it. The repo owner can then look through the changes and decide whether to accept them or not — nothing joins main automatically.

**As Collaborator**: go to your partner's repo — a banner should offer "Compare & pull request" for your branch. Click it, add a short description, `Create pull` request.
**As Repo Owner**: go to your own repo's `Pull requests` tab, open your partner's PR, look at `Files changed` to see exactly what's being added, then click `Merge pull request`.

By the end, both repos should contain two (or more) datasets' worth of notebooks/data/results.

Finally, explore the commit history of your repository. Make sure you can trace back the changes you made when uploading and editing files, as well as when your partner uploaded their own data. Could you figure out the history of the project if someone (Reviewer 3) asked you an awkward question? How does this compare to other methods of version control?
