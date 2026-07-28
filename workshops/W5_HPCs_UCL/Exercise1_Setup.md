## Logging in and setting up a directory
First, we will log in following these [instructions](https://github-pages.arc.ucl.ac.uk/hpc-intro/11-connecting/index.html) and [have a look around](https://github-pages.arc.ucl.ac.uk/hpc-intro/12-cluster/index.html). Make a project folder and move to it:

```
mkdir my_project_dir
cd my_project_dir
```

## Clone your git repository
Then clone your repository: `git clone https://github.com/YOUR-REPO-PATH` (remember to change the path to your repository) to get your code onto the HPC.

Why wouldn't we just copy over the relevant files??

## Make an environment using the conda "module"
We will discuss how programmes are setup on HPCs as "modules" and how we can use them following [these notes](https://github-pages.arc.ucl.ac.uk/hpc-intro/15-modules/index.html).

We will use the conda module to create an environment that matches the one we set up locally:

```
COMMANDS
```
### Copy in some data
Find the RDSS file location and copy some data to a data folder:

```
mkdir -p data/input
cp /PATH/TO/RDSS/PROJECT data/input
```

Now you should have all the code, libraries and data needed to run your analysis on the HPC!
