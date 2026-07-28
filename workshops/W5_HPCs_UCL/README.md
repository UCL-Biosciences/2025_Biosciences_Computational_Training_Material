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
- laptop memory isn't needed for big processes so you can use it normallypar

## Exercises overview

**Exercise 1 — cluster setup** First we will get ourselves onto the cluster and set up everything we need - code, environment and data.

### Logging in and setting up a directory
First, we will log in following these [instructions](https://github-pages.arc.ucl.ac.uk/hpc-intro/11-connecting/index.html) and [have a look around](https://github-pages.arc.ucl.ac.uk/hpc-intro/12-cluster/index.html). Make a project folder and move to it:

```
mkdir my_project_dir
cd my_project_dir
```

### Clone your git repository
Then clone your repository: `git clone https://github.com/YOUR-REPO-PATH` (remember to change the path to your repository).

### Make an environment using the conda "module"
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



**Exercise 2 — Submit a job.** Bring your data onto the cluster from RDSS, then work through the two prepared scripts: the Python script to run, and the SGE submission script that describes it to the scheduler. We walk the submission script line by line — the resource requests (`h_rt`, `mem`), the working directory, activating the environment, the call to run the script — because this is the genuinely new concept of the day. Submit with `qsub`, watch it in the queue with `qstat`, then retrieve the results back to your own machine.

A pre-provisioned checkpoint copy of the project (repo + environment + data, ready to go) is available to `cd` into, so anyone whose own setup failed at an earlier step can still reach the batch-submission payoff.

## Wrap-up

We return to the "who does this help?" table from Week 3, extended one more time via an anonymous Menti check-in: for the work you actually do, **when would you reach for an HPC — and who does that help: yourself, your collaborators, the wider community?** The cumulative table is revealed at the end, tying the session's mechanics back to the reproducibility and data-management themes running through the whole course.

The closing note is honest: today's job was a toy. But you now hold the full path — connect, move your project, build your environment, submit, retrieve — so that when a real wall hits, the cluster is a tool you already know how to use.
