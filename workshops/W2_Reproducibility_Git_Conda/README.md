# Week 2 - Git/GitHub and Environments

## Git/GitHub

### Setup
- [GitHub account](https://github.com/signup)
- git installed in your laptop
    - Windows: Follow the [Bash shell installation instructions](https://carpentries.github.io/workshop-template/#the-bash-shell) (under the Git for Windows tab)
    - Mac:
        - Open a terminal window
        - Type:
      ```
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      ```
        - Follow the installation prompts
        - Once it's installed, run: `brew install git` to install git.
- [Download VS Code](https://code.visualstudio.com/download) 

### Learning Objectives

After this session, you should be able to

- *understand* the github workflow to contribute to a repository
- *modify* and **create** pages on a repository using github and/or codespaces
- *use* VS Code to interact with a github repository


### GitHub

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

#### Exercise 1 - Setting up a github repository (75 mins)
##### Making a repo online
First, we will **make a git repository** on the github webpage (5 mins)
1. Navigate to [github.com](https://github.com/) and login (or create an account)
2. Click on `Repositories` tab and click `New`. Add a name for the repo and short description. Click `create repository`. Look around - make yourself at home!

##### Connecting the online repo to your computer
But our work and files are saved to our computer locally. We need to connect the repository made on github to our local computer. To do this, we **"clone" the online repo to our computer.**

To do this, we will use **Visual Studio Code**. This is a handy platform that allows you to explore folders, edit files and run code in a single window. It also has lots of useful "extensions" to help your computational life run smoothly. So, a quick detour:
1. Open visual studio code and click on `Open Folder`. Navigate to the folder you worked in last week and open it.
2. In the top bar (File, Edit etc), click on `Terminal` > `New Terminal`. Then, a fiddly bit. This terminal session must be bash (or git bash). In Windows, the default terminal is often powershell. To open a bash terminal, click on the little downwards arrow which is in the top right of the terminal window, next to where it says powershell. If it says bash or git bash already, you can go to the next section.

Now we are ready to **"clone" our repo**. The repo will be cloned (downloaded) to where you selected when you clicked `Open Folder` - make sure this is a suitable location:
1. To get the address of the github repository, go the repo page, click on the big green `Code` button. Make sure you are on the `HTTPS` tab, and copy the URL in the middle of the box. It will be `https://github.com/<username>/<reponame>.git`
1. Back in the terminal window, enter `git clone https://github.com/<username>/<reponame>.git` (with the correct username and repo name) and press enter.

##### Adding files to the repo
We are going to add the code, data and outputs from last week. To simulate a real example, we will have two versions - the "wrong" data and the "correct" data. And get a recap on last week while we are here.

1. Go to the notebook you made last week. Edit the file path to the original dataset and re-run the notebook. Make sure the outputs are saved.
2. Open File Explorer and move the notebook, data and outputs into the local clone of the repo (made in previous step).
3. Go back to the Visual Studio Code terminal. Important step! You will need to move to the folder. Click open folder again, navigate to the clone of the repo and open. Repeat the steps above to open a new terminal window.
4. Check the status of the repo by running `git status`. It should tell you that there are some new files added! Which tells us git has noticed the files have been created (or moved into the folder). To register (track) the files needs two steps. First `git add filename`, then `git commit -m "initial commit"`.

Adding files tells git to find the files you want to change and record the info about what changes have been made. You can add lots of files at once. Committing changes is what generates a snapshot of the repository and records all the information about changes that have been made since the last commit. So `add` and `committ` work together closely, but do different jobs.

Finally, run `git push` to send the new files and all the information in the commit to the "remote" repository on 

##### Connecting the online repo to your computer


##### Connecting the online repo to your computer














We've got a cities folder in our repository with a set of files separated by continents and countries directories. Go to the file assigned to you (see below) and, in pairs, change at least two of the `FIXME` in the file:
- write in the file the name of that city in one of their local languages or the pronunciation (You'll find that information on wikipedia);
- Add a reason of what to see in that city;
- Update the link to wikipedia.

Try to use any of the [available styling text syntax available in markdown files](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#styling-text).

> [!NOTE]
> You can add web links in markdown files following this syntax:
> 
> ```markdown
> You can visit [website title](https://web.site/pointed/to).
> ```
> 
> If you need to link to the same page multiple times in the same file or the link makes the text less readable, you can use reference-style links as:
> 
> ```markdown
> You can visit [our website][main-website] to find information about our activities and events.
> 
> If you'd like to work with us, our [main page][main-website] also contains a list of open positions.
> 
> 
> [main-website]: https://our.web.site/
> ```

##### Exercise 2 - Review contributions

Choose one of the pull-request listed above (from a different person that your
pair), add your name afterwards, and review the pull request as shown by the
instructor.
If you are happy with the changes, *approve* it, otherwise, *request changes* to
make it better. Don't forget to thank them for their contribution.

After approving it, press the <kbd>merge</kbd> button that is now available.

##### Exercise 3 - Add a file: a new traveller

Under the `travellers` directory create a new file as demonstrated with your name or one of a traveller you'd like that join us.

The file needs to have a `qmd` extension: `example.qmd`.

> [!WARNING]
> 
> Avoid spaces in the name, use `CamelCase` or `snake_case` if you want to put many words together. For example `sara_alfarsi.qmd`.
> 

Use the following code snippet as a template for the file, so it is rendered nicely on our website. See the existing ones for inspiration. This is using a [Quarto template](https://quarto.org/docs/websites/website-about.html)

    ---
    title: "FIXME - Name"
    subtitle: "FIXME - characteristic"
    image: FIXME - photo url
    toc: false
    about:
      id: person-profile
      template: jolla
    ---

    ```{=html}
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="../travellers.html">Travellers</a></li>
        <li class="breadcrumb-item active" aria-current="page">{{< meta title >}}</li>
      </ol>
    </nav>
    ```

    :::{#person-profile}
    :::

    ## Biography

    FIXME: add a one line description about the person

    ## Travelled cities

    - FIXME - add cities visited.
    - FIXME - city 2
    - FIXME - city 3

Commit the changes and create a pull request. Add your link to the collaborative document to get someone to review it (add your name when you pick one).

##### Pre-Exercise 4 - configure git locally

This step we need to do it only once, the first time we are using git on our computer.

Open a terminal (gitbash if you are using windows) and type:

```
git config --global user.name "Your Name"
git config --global user.email "your.@email.com"
```

`git config --list` will show you that the details you have entered are OK.


##### Exercise 4 - Make changes locally

When editing in github you had seen a message saying that you can't write in `main` and create a branch for the review process automatically. When we work locally that doesn't happen automatically. Therefore, we need to create a branch first, and then push the changes after committing it.

But first, we need to get the repository locally!

- Open VS Code
- ![](https://raw.githubusercontent.com/microsoft/vscode-icons/main/icons/light/source-control.svg) Click in the source control icon (third icon from the top in the left bar).
- Select <kbd>Clone Repository</kbd> and pick ":octocat: Clone from GitHub"
- Follow the Authentication prompt: Allow VS Code to sign in on GitHub and accept the following screens on your default browser.
- Back in VSCode, select the repository we've been working with.
- Select where you'd like to save that repository on your computer.
- Find the `branches` tab at the bottom of the window, and click `+`. Write a name for your branch in the popup that appears in the top. e.g., `your_ghusername-code`.
- ![](https://raw.githubusercontent.com/microsoft/vscode-icons/main/icons/light/files.svg) Find the `.qmd` file you want to edit or create (first icon from the top in the left bar). You can create one new like `researchers.qmd` but with your name `sarah_results.qmd`.
- Edit the `.qmd` file, add the code snippet you want to. Check [quarto documentation on adding a python file](https://quarto.org/docs/computations/python.html) and [matplotlib gallery](https://matplotlib.org/stable/gallery/index.html) for examples.
- Optional: Click on the `preview` button in the top right corner of the editor, and tweak as desired. You'll need Quarto and Quarto extension installed.
- Save the file
- ![](https://raw.githubusercontent.com/microsoft/vscode-icons/main/icons/light/source-control.svg) Click in the source control, find the file you modified listed under the `changes` menu, and click `+` to add the file.
- Write a message on the box above the `Commit` button, and press the <kbd>✔️ Commit</kbd> button.
- The Commit button will then change to <kbd>🔃 Sync changes</kbd>, press it to propagate the changes to github.
- Open a pull-request (either from the pop-up or on GitHub)

##### Exercise 5 - Create a repository from scratch

- Open VS Code
- Open the folder of a particular project you are working on (your thesis, a project, something new, last week python folder)
- ![](https://raw.githubusercontent.com/microsoft/vscode-icons/main/icons/light/source-control.svg) Click in the source control icon (third icon from the top in the left bar).
- Select <kbd>Initialize Repository</kbd>
- Add the files you want to the repository
- Publish it to GitHub, select a Public/Private repository as you'd like
- Put the blue post it when done.

## Python environments

### Setup
- Install miniforge (or any other conda distribution)
- Install VS Code

### Learning Objectives

After this session, you should be able to

- *understand* why environments are useful in research software
- **create** and **share** your own environment
- *use* VS Code to interact with Python environments

### Discussion - Environments

What do you think environments are? Why would we need them?

### Python Environments

<details><summary>What?</summary> To keep the tools we need, like a Lab</details>

<details><summary>Why?</summary>  Because we want the lab be used by the same tools for our experiments</details>

<details><summary>How?</summary>  Conda is one of many ways, and the easier to get started with</details>

#### Conda Environments

Last week we asked you to install the an environment. Let's create now our own:

```
conda create -n project-dna pandas=2.3.3
```

To work on it you need to activate it first

```
conda activate project-dna
```

and to deactivate it is:

```
conda deactivate
```

To add other libraries we do, in the preferred environment:

```
conda install [-n project-dna] jupyter
```

To share the environment we can generate a yaml file with the environment properties:

```
conda export --file=project-dna.yaml
```

To "import" a shared environment we do:

```
conda env create -f project-dna.yaml
```

This file is like the one we used last week... but a lot larger.
Let's look how the file is composed:

```
name: env-name
channels:
  - conda-forge
dependencies:
  - dependency_1
  - dependency_2
  - dependency_3=2.3.1
```



#### Discussion - Why are so different?

Discuss within your groups why the files (last week and recently created) are so different if both provides `pandas` and `jupyter`.


#### Environments on VS Code

When working on a project, we may want to run things from within VSCode. 

- Open the folder from last week on VS Code.
- Open one of the notebooks
- Choose the new conda environment (right hand-corner Select Kernel)
- Run All - is still working?
- select "Export" under the `...` at the top of the notebook, and choose "Python Script"
- save that new file
- Select the environment on the bottom left corner

#### Exercise - VS Code and Python

- Create a new notebook (create a file with `.ipynb` extension) or create a new python script (a file with `.py` extension)
- Add some code, copy an example from [matplotlib gallery](https://matplotlib.org/stable/gallery/index.html)
- Select the environment as required to run that file
- Run that file
