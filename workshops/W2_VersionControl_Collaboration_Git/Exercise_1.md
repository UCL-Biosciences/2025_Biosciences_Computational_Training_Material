### Exercise 1 - Setting up a github repository (60-75 mins)
#### Making a repo online (5 mins)
First, we will **make a git repository** on the github webpage
1. Navigate to [github.com](https://github.com/) and login (or create an account)
2. Click on `Repositories` tab and click `New`. Add a name for the repo and short description. Click `create repository`. Look around - make yourself at home!

#### Connecting the online repo to your computer (15 mins)
But our work and files are saved to our computer locally. We need to connect the repository made on github to our local computer. To do this, we **"clone" the online repo to our computer.**

To do this, we will use **Visual Studio Code**. This is a handy platform that allows you to explore folders, edit files and run code in a single window. It also has lots of useful "extensions" to help your computational life run smoothly. So, a quick detour:
1. Open visual studio code and click on `Open Folder`. Navigate to the folder you worked in last week and open it.
2. Log in to github inside Visual Studio Code. Click on the accounts button in the bottom-left (circle with a person's head in it), above settings icon. Sign in with or to github and follow the instructions in the browser pop-up to authorise VSC to sign in to your github.

(For VSC desktop only, no terminals in VSC web:)

3. In the top bar (File, Edit etc), click on `Terminal` > `New Terminal`. Then, a fiddly bit. This terminal session must be bash (or git bash). In Windows, the default terminal is often powershell. To open a bash terminal, click on the little downwards arrow which is in the top right of the terminal window, next to where it says powershell. If it says bash or git bash already, you can go to the next section.
4. Finally, we set up a couple of things in our git account. This just ensures any changes we make are linked to our github account - use the same email you signed up to git with:
```
git config --global user.name "Your Name"
git config --global user.email "your.@email.com"
```

`git config --list` will show you that the details you have entered are OK.

Now we are ready to **"clone" our repo**.
1. In Visual Studio Code, `Ctrl/Cmd+Shift+P` → `Git: Clone`. If you have logged in successfully, you should be able to search for the repo you made earlier
2. Select the training repo and clone it to where ever you are working on your laptop. Select "Cancel" to keep your current folder open.

#### Adding files to the repo (20 mins)
We are going to add the code, data and outputs from last week. To simulate a real example, we will have two versions - the "wrong" data and the "correct" data. And get a recap on last week while we are here.

1. Go to the notebook you made last week. Edit the file path to the original dataset and re-run the notebook. Make sure the outputs are saved.
2. In Visual Studio Code's explorer panel, move the notebook, data and outputs into the local clone of the repo (made in previous step).
3. Find the `Source Control` icon on the left hand side (<img width="25.4" height="25.4" alt="image" src="https://github.com/user-attachments/assets/bc9ffeb9-d358-400c-9339-d12257525abd" />) and you should see all the files you moved listed as 'Changes'. This means git has found the new files and is ready to add them to the repo = start "tracking" them.
4. Type a message in the box at the top of 'Source Control' e.g. "first commit", click 'Commit' and click on 'Yes'. This will add all the files to the repository and git will now track all changes to them.
5. Click on "Sync Changes" and "OK" to push the changes to the remote repository i.e. the one on github.com.

Adding files tells git to find the files you want to change and record the info about what changes have been made. You can add lots of files at once. Committing changes is what generates a snapshot of the repository and records all the information about changes that have been made since the last commit. 

**Authentication**. If you have not signed in to github in Visual Studio Code, you will need to do it before you can `push`. Sign in via the Accounts icon bottom-left of VS Code.

#### Making and recording changes (15 mins)
OK let's continue simulating the "real" scenario. Your (favourite) collaborator has just sent the correct dataset and you need to update all the results. You can do that easily (because you wrote reusable code :D) but don't want to throw away the original results in case you want to refer back to them later.

Because those files were pushed to git, that info will be stored as long as the repo exists. Note, that is why we never upload personal/sensitive/private data to repos that might later be made public. Or equally, we don't make public any repos that previously contained data that could be found in the commit history.

So, go to the notebook again. Read in the correct dataset, re-run the code and save new outputs. No need to change the names of the output files!

Then, return to Visual Studio Code and make sure the edited files are shown in the `Source Control` icon on the left hand side (<img width="25.4" height="25.4" alt="image" src="https://github.com/user-attachments/assets/bc9ffeb9-d358-400c-9339-d12257525abd" />). This should include the notebook(s) you edit and any outputs you saved.

Write a message, commit the changes, and push (sync) them to the github repo. Done!

#### Viewing changes on github (10 mins)
Go to the repo online and see what changes you can find:
- do the files look different?
- Can you find the list of previous commits?
- Can you find the changes that were made during the last commit?

#### Summary (5 mins)
Wowzers! That could have been a disaster! But because we had traceable, reusable code, it was easy to do everything again. And because we version controlled everything with git, we know exactly what the results look like with both datasets, and can look at both versions to understand differences. And this is only part 1! Huzzah!
