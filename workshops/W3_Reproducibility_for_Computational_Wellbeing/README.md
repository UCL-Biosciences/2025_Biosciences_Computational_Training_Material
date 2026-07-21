This week, we discussed a range of ideas related to data and project management, including being FAIR and reproducible, as well as making our own lives easier.

The slides were shared internally but not ready to be shared publicly yet. We will add a link here if/when they are made available.



## Environments with python and conda

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
