# Week 2 - Git and Github: Reproducibility, Version Control and Collaboration
## Learning Objectives

- understand what git offers to researchers and what problem(s) it solves
- Set up a git account and start version control for the files from w1
- Make changes and see how history is recorded
- see how you can collaborate with colleagues on a shared repo

## GitHub

Before getting to GitHub, let's see how a collaboration flow works on MS Word

![image](https://hackmd.io/_uploads/r1n291Wf0.png)

When using git there are a couple of differences.
- changes are grouped and can cover multiple files.
- Each set of changes contain a description that's kept in the history (who made the change, why, what and when).
- You can contribute to any public repository, but only the owners of that repository can accept (merge) these changes.
- The review process happens on a "Pull request".
 
📦 Our repository for today: [`UCL-Biosciences/FIXME202405-arcgit-workshop`](https://github.com/...FIXME/)

### Exercises

We'll break this down into two exercises. First for setting a repo up for managing a project, then for collaboration.

The first will be done individually, the second in pairs/groups. The isntructor will demo all the steps though and participants will follow along.

### Exercise 1 - Setting up a github repository (~75 mins)
#### Making a repo online (5 mins)
First, we will **make a git repository** on the github webpage
1. Navigate to [github.com](https://github.com/) and login (or create an account)
2. Click on `Repositories` tab and click `New`. Add a name for the repo and short description. Click `create repository`. Look around - make yourself at home!

#### Connecting the online repo to your computer (15 mins)
But our work and files are saved to our computer locally. We need to connect the repository made on github to our local computer. To do this, we **"clone" the online repo to our computer.**

To do this, we will use **Visual Studio Code**. This is a handy platform that allows you to explore folders, edit files and run code in a single window. It also has lots of useful "extensions" to help your computational life run smoothly. So, a quick detour:
1. Open visual studio code and click on `Open Folder`. Navigate to the folder you worked in last week and open it.
2. Log in to github inside Visual Studio Code. Click on the accounts button in the bottom-left (circle with a person'a head in it), above settings icon. Sign in with or to github and follow the instructions in the browser pop-up to authorise VSC to sign in to your github.
3. In the top bar (File, Edit etc), click on `Terminal` > `New Terminal`. Then, a fiddly bit. This terminal session must be bash (or git bash). In Windows, the default terminal is often powershell. To open a bash terminal, click on the little downwards arrow which is in the top right of the terminal window, next to where it says powershell. If it says bash or git bash already, you can go to the next section.
4. Finally, we set up a couple of things in our git account. This just ensures any changes we make are linked to our github account - use the same email you signed up to git with:
```
git config --global user.name "Your Name"
git config --global user.email "your.@email.com"
```

`git config --list` will show you that the details you have entered are OK.


Now we are ready to **"clone" our repo**. The repo will be cloned (downloaded) to where you selected when you clicked `Open Folder` - make sure this is a suitable location:
1. To get the address of the github repository, go the repo page, click on the big green `Code` button. Make sure you are on the `HTTPS` tab, and copy the URL in the middle of the box. It will be `https://github.com/<username>/<reponame>.git`
2. Back in the terminal window, enter `git clone https://github.com/<username>/<reponame>.git` (with the correct username and repo name) and press enter.

#### Adding files to the repo (20 mins)
We are going to add the code, data and outputs from last week. To simulate a real example, we will have two versions - the "wrong" data and the "correct" data. And get a recap on last week while we are here.

1. Go to the notebook you made last week. Edit the file path to the original dataset and re-run the notebook. Make sure the outputs are saved.
2. Open File Explorer and move the notebook, data and outputs into the local clone of the repo (made in previous step).
3. Go back to the Visual Studio Code terminal. Important step! You will need to move to the folder. Click open folder again, navigate to the clone of the repo and open. Repeat the steps above to open a new terminal window.
4. Check the status of the repo by running `git status`. It should tell you that there are some new files added! Which tells us git has noticed the files have been created (or moved into the folder). To register (track) the files needs two steps. First `git add filename`, then `git commit -m "initial commit"`.

Adding files tells git to find the files you want to change and record the info about what changes have been made. You can add lots of files at once. Committing changes is what generates a snapshot of the repository and records all the information about changes that have been made since the last commit. So `add` and `committ` work together closely, but do different jobs.

Finally, run `git push` to send the new files and all the information in the commit to the "remote" repository on github.

**Authentication**. If you have not signed in to github in Visual Studio Code, you will need to do it before you can `push`. Sign in via the Accounts icon bottom-left of VS Code.

#### Making and recording changes (15 mins)
OK let's continue simulating the "real" scenario. Your (favourite) collaborator has just sent the correct dataset and you need to update all the results. You can do that easily (because you wrote reusable code :D) but don't want to throw away the original results in case you want to refer back to them later.

Because those files were pushed to git, that info will be stored as long as the repo exists. Note, that is why we never upload personal/sensitive/private data to repos that might later be made public. Or equally, we don't make public any repos that previously contained data that could be found in the commit history.

So, go to the notebook again. Read in the correct dataset, re-run the code and save new outputs. No need to change the names of the output files!

Then, return to Visual Studio Code and the git bash terminal window, and send the changes to github by adding, committing and pushing.

#### Viewing changes on github (10 mins)
Go to the repo online and see what changes you can find:
- do the files look different?
- Can you find the list of previous commits?
- Can you find the changes that were made during the last commit?

#### Summary (5 mins)
Wowzers! That could have been a disaster! But because we had traceable, reusable code, it was easy to do everything again. And because we version controlled everything with git, we know exactly what the results look like with both datasets, and can look at both versions to understand differences. And this is only part 1! Huzzah!

_____

### Exercise 2 - Collaborating via GitHub (60 mins)
#### Finding a group (5 mins)
Form a group with someone working on a different dataset to yours. Groups can be 2 or more people, as long as there are people working on at least 2 different datasets.

You'll both do every step below — each of you is Repo Owner (for your own repo) and Collaborator (for your partner's repo) at the same time.

#### Giving each other access (5 mins)

Go to your own repo → Settings → Collaborators → Add people. Search your partner's GitHub username and send the invite.
Check your email / GitHub notifications bell for your partner's invite and accept it.

This can take a couple of minutes to come through. While you wait, look at your collaborators repo. Does it look the same as yours? How is it different?

#### Creating a branch on your partner's repo (5 mins)
We're about to send our work and changes to a colleague's repo. If we send it directly, it risks messing up what's already there — especially if the code works and is actually being used or relied on by others. You can't go messing up someone's working pipeline!

It's safer to send our changes to a secure, separate working copy first, before anything gets added to the main repo. So we make a working copy of the repo — called a branch — and send our changes there instead of straight to main. The repo owner can then review the changes and decide whether to accept them or not, without main ever being at risk.

1. On your partner's repo page, click the branch dropdown (usually says `main`) → type a new branch name, e.g. `<your-name>-data` → `Create branch`
2. Make sure the branch selector now shows your new branch, not main

#### Adding your files (10 mins)
Still on your partner's repo, on your new branch:
1. Click `Add file` → `Upload files`. `Add file` is to the left of the big green `Code` button and sometimes minimises to a `+` symbol
2. Drag in your notebook, dataset, and output files from last week (and earlier, if relevant)
3. Scroll down, add a short commit message, confirm you're committing to your branch (not main), click Commit changes

#### Opening and merging the Pull Request (15 mins)

We've made our changes safely on a separate branch — now we want to bring them into main. But we shouldn't just merge them in blindly; the repo owner hasn't actually seen what's being added yet, and main is the version other people trust and rely on.

It's safer to have a formal review step before anything joins main — a chance for the repo owner to look over exactly what's changed and confirm it's good to bring in. This is called a Pull Request (PR): a formal request to merge your branch into main, which sits open for review until someone with permission accepts it. The repo owner can then look through the changes and decide whether to accept them or not — nothing joins main automatically.

**As Collaborator**: go to your partner's repo — a banner should offer "Compare & pull request" for your branch. Click it, add a short description, `Create pull` request.
**As Repo Owner**: go to your own repo's `Pull requests` tab, open your partner's PR, look at `Files changed` to see exactly what's being added, then click `Merge pull request`.

By the end, both repos should contain two (or more) datasets' worth of notebooks/data/results.

#### Wrap-up discussion (5 mins)

Now your repo has multiple different datasets in it — does the same code/workflow structure make sense for both?
What would this have looked like over email instead?
Why might a branch + PR be safer than uploading straight to main, even without a conflict?

And crucially, git requires some learning; do you think it will be worth it based on what you've seen so far?!

## What's next?
Now you've got a version-controlled, collaboratively-reviewed project with two analyses sitting in it. But version control on its own doesn't guarantee someone else (or future-you) can actually understand or run what's in there. Next week we'll pick up exactly where this leaves off: making sure the code, data, and environment behind a project are genuinely reproducible — for yourself, for collaborators like the one you just worked with, and for the wider research community — using good research data management, FAIR principles, and our institutional storage systems.


