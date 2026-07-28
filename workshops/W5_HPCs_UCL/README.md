# High Performance Compute at UCL
Last week, we applied machine learning to our data and found that it was very slow to run the full analysis on our laptops. Some analyses require too much compute to run on our "local" computers. UCL has a number of High Performance Compute (HPC) clusters that we can use when we need more compute power. Today we will look at how we can run some of our analyses on UCL HPCs.

## Learning objectives

By the end of this session, participants will be able to:
- Explain what problem an HPC solves and when it is (and isn't) the right tool
- Connect to the cluster and navigate the filesystem from the command line
- Move a project onto the cluster by cloning a GitHub repository
- Build a working environment on the cluster from a Conda export
- Bring data onto the cluster
- Write and submit an SGE batch job, and monitor it in the queue
- Retrieve results back to their own machine

## Session plan (3 hours)

| Activity | Time |
|----------|------|
| Why HPC? | 15 min |
| Log in | 20 min |
| Get your code (github) onto the cluster | 10 min |
| Break | 10 min |
| Build your environment | 10 min |
| Transfer data  | 20 min |
| Jobs | 45 min |
| Break | 10 min |
| Download results to your computer | 10 min |
| wrap-up | 10 min |

## Intro activity — why use HPCs?
HPCs are important when we need more compute power. Let's see if any of the participants have run into power problems: menti quiz. [Link] and QR code:

The questions (mostly in case menti doesn't work):
- You start a programme or hit run and your laptop is slow/unusable until it has finished
- Started a big job (e.g. doing analysis, downloading data), only to find the computer turned off before you finished and you have to start again
- Dataset too big and won't even load
- You need to run the same analysis across 200 samples and have to do it one at a time

HPCs address some of these problems:
- bigger computers
- jobs run independently so you can walk away or turn off your laptop
- laptop memory isn't needed for big processes so you can use it normally

## Exercises overview

**Exercise 1 — cluster setup** [First](https://github.com/UCL-Biosciences/Biosciences-Computational-Training/blob/prep-2026/workshops/W5_HPCs_UCL/Exercise1_Setup.md) we will get ourselves onto the cluster and set up everything we need - code, environment and data.

**Exercise 2 — Submit a job.** Now we will look at [HPC nodes](https://github-pages.arc.ucl.ac.uk/hpc-intro/12-cluster/index.html#nodes) and the difference between login and compute nodes.

Then we will look at [job scripts](https://github-pages.arc.ucl.ac.uk/hpc-intro/13-scheduler/index.html), which is how we tell the cluster what we want to do.

Now, we will submit the python code we wrote in week 1 as a job. First, [convert the notebook to a python file](https://code.visualstudio.com/docs/python/jupyter-support-py#_convert-jupyter-notebooks-to-python-code-file). Have a look at the python (`.py`) file - how is it different to the notebook? Why would these differences be needed in order to submit the code as a job on an HPC?

To run the python script (`.py`) from within the job script (`.sh`), we add this to your job script:

```
## load modules

## activate your environment

## run the code
python /path/to/script.py
```

Finally, download the output and check it on your local computer. You can download it in Visual Studio Code by right-clicking on a file and selecting `Download` - simples!

## Wrap-up
To finish, let's trace your project all the way through, because the weeks were really one story:

Week 1 — Coding: you took raw data in, wrangled it, made a figure, and saved your results — a working analysis.
Week 2 — Version control & collaboration: you tracked your changes and shared your work, turning a file on your laptop into a repository others can see and build on.
Week 3 — Reproducibility: you made it something anyone can rerun — an environment they can rebuild, data looked after in RDSS, a project someone else could actually pick up.
Week 4 — Scaling up: you took that same project onto a cluster and ran it at a scale your laptop couldn't manage.

Each week solved a problem the week before created. Code needs versioning; versioned code needs a reproducible environment; a reproducible environment is what lets your work run somewhere bigger. You leave with a template project that holds all of it.

Please complete post-training survey! Link to be added.




