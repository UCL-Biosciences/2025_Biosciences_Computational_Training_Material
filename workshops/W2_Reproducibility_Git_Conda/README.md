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

#### Exercises

Exercise will be done in pairs. Even though you do them in pairs, most of the exercises are supposed to be done by both members. First one person writes and the other observes, and then you swap roles.

##### Exercise 1 - You and a city (modify a file adding more info about the cities)

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
