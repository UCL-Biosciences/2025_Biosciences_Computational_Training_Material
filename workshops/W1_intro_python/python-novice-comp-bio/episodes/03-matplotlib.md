---
title: Visualizing Tabular Data
teaching: 30
exercises: 20
---

::::::::::::::::::::::::::::::::::::::: objectives

- Plot simple graphs from data.
- Plot multiple graphs in a single figure.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can I visualize tabular data in Python?
- How can I group several plots together?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Visualizing data

The mathematician Richard Hamming once said, "The purpose of computing is insight, not numbers,"
and the best way to develop insight is often to visualize data.  Visualization deserves an entire
lecture of its own, but we can explore a few features of Python's `matplotlib` library here.  While
there is no official plotting library, `matplotlib` is the *de facto* standard.  First, we will
import the `pyplot` module from `matplotlib` and use two of its functions to create and display a
[heat map](../learners/reference.md#heat-map) of our data:

::::::::::::::::::::::::::::::::::::::::::  prereq

## Episode Prerequisites

If you are continuing in the same notebook from the previous episode, you already
have a `data` variable and have imported `numpy`.  If you are starting a new
notebook at this point, you need the following two lines:

```python
import numpy
data = numpy.loadtxt(fname='../data/molerat_activity_v1.csv', delimiter=',')
```

::::::::::::::::::::::::::::::::::::::::::::::::::

```python
import matplotlib.pyplot
image = matplotlib.pyplot.imshow(data, aspect='auto')
matplotlib.pyplot.show()
```

![](fig/activity-01-imshow.svg){alt='Heat map representing the data variable. Each cell is colored by value along a color gradient from blue to yellow.'}

Each row in the heat map corresponds to a mole-rat in the behaviour dataset, and each column
corresponds to a day in the dataset.  Blue pixels in this heat map represent low values, while
yellow pixels represent high values.  As we can see, the general amount of activity is lower in the top ~100 rows than the rest.

So far so good as this is in line with our knowledge of naked mole-rat colonies. The top 100 rows are breeders, who do all the reproduction in a colony but much less working behaviour.

Now let's take a look at the average activity over time:

```python
ave_day = numpy.mean(data, axis=0)
ave_day_plot = matplotlib.pyplot.plot(ave_day)
matplotlib.pyplot.show()
```

<img width="545" height="413" alt="image" src="https://github.com/user-attachments/assets/d6e7021b-5295-426b-bcfb-a2f0daa19ed0" />
{alt='A line graph showing the average activity across all mole-rats over a 30-day period.'}

Here, we have put the average activity per day across all mole-rats in the variable
`ave_activity`, then asked `matplotlib.pyplot` to create and display a line graph of those
values. It is quite variable - even naked mole-rats need days off!

But that is not what we are really interested in. We want to know if there are any differences in behaviour between breeders and non-breeders. We plot the average per individual, this time taking the average per row across all columns so `axis=1`.

```python
ave_MR = numpy.mean(data, axis=1)
ave_MR_plot = matplotlib.pyplot.plot(ave_MR)
matplotlib.pyplot.show()
```

<img width="543" height="413" alt="image" src="https://github.com/user-attachments/assets/9df6bdd1-fcd5-4c7a-98c5-222b6ec0e50e" />
{alt='A line graph showing the average activity per individual.'}

```python
min_plot = matplotlib.pyplot.plot(numpy.min(data, axis=1))
matplotlib.pyplot.show()
```

<img width="556" height="413" alt="image" src="https://github.com/user-attachments/assets/09f7b516-4931-4f7a-b939-1d66178c1aa1" />
{alt='A line graph showing the minimum activity per mole-rat.'}

Looks like it is pretty clear; while the average amount of activity varies over time, the breeders (top 100 rows) are consistently less active. Must be busy seeing to important business..

### Grouping plots

You can group similar plots in a single figure using subplots.
This script below uses a number of new commands. The function `matplotlib.pyplot.figure()`
creates a space into which we will place all of our plots. The parameter `figsize`
tells Python how big to make this space. Each subplot is placed into the figure using
its `add_subplot` [method](../learners/reference.md#method). The `add_subplot` method takes
3 parameters. The first denotes how many total rows of subplots there are, the second parameter
refers to the total number of subplot columns, and the final parameter denotes which subplot
your variable is referencing (left-to-right, top-to-bottom). Each subplot is stored in a
different variable (`axes1`, `axes2`, `axes3`). Once a subplot is created, the axes can
be titled using the `set_xlabel()` command (or `set_ylabel()`).
Here are our three plots side by side:

```python
import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='../data/molerat_activity_v1.csv', delimiter=',')

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=1))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=1))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=1))

fig.tight_layout()

matplotlib.pyplot.savefig('activity.png')
matplotlib.pyplot.show()
```

<img width="988" height="290" alt="image" src="https://github.com/user-attachments/assets/593f42ec-8fa8-4f6c-89e8-46c51a066e4b" />{alt='Three line graphs showing the daily average, maximum and minimum activity over a 40-day period.'}

The [call](../learners/reference.md#function-call) to `loadtxt` reads our data,
and the rest of the program tells the plotting library
how large we want the figure to be,
that we're creating three subplots,
what to draw for each one,
and that we want a tight layout.
(If we leave out that call to `fig.tight_layout()`,
the graphs will actually be squeezed together more closely.)

The call to `savefig` stores the plot as a graphics file. This can be
a convenient way to store your plots for use in other documents, web
pages etc. The graphics format is automatically determined by
Matplotlib from the file name ending we specify; here PNG from
'activity.png'. Matplotlib supports many different graphics
formats, including SVG, PDF, and JPEG.

:::::::::::::::::::::::::::::::::::::::::  callout

## Importing libraries with shortcuts

In this lesson we use the `import matplotlib.pyplot`
[syntax](../learners/reference.md#syntax)
to import the `pyplot` module of `matplotlib`. However, shortcuts such as
`import matplotlib.pyplot as plt` are frequently used.
Importing `pyplot` this way means that after the initial import, rather than writing
`matplotlib.pyplot.plot(...)`, you can now write `plt.plot(...)`.
Another common convention is to use the shortcut `import numpy as np` when importing the
NumPy library. We then can write `np.loadtxt(...)` instead of `numpy.loadtxt(...)`,
for example.

Some people prefer these shortcuts as it is quicker to type and results in shorter
lines of code - especially for libraries with long names! You will frequently see
Python code online using a `pyplot` function with `plt`, or a NumPy function with
`np`, and it's because they've used this shortcut. It makes no difference which
approach you choose to take, but you must be consistent as if you use
`import matplotlib.pyplot as plt` then `matplotlib.pyplot.plot(...)` will not work, and
you must use `plt.plot(...)` instead. Because of this, when working with other people it
is important you agree on how libraries are imported.


::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Plot Scaling

Why do all of our plots stop just short of the upper end of our graph?

:::::::::::::::  solution

## Solution

Because matplotlib normally sets x and y axes limits to the min and max of our data
(depending on data range)


:::::::::::::::::::::::::

If we want to change this, we can use the `set_ylim(min, max)` method of each 'axes',
for example:

```python
axes3.set_ylim(0, 6)
```

Update your plotting code to automatically set a more appropriate scale.
(Hint: you can make use of the `max` and `min` methods to help.)

:::::::::::::::  solution

## Solution

```python
# One method
axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=1))
axes3.set_ylim(0, 6)
```

:::::::::::::::::::::::::

:::::::::::::::  solution

## Solution

```python
# A more automated approach
min_data = numpy.min(data, axis=q)
axes3.set_ylabel('min')
axes3.plot(min_data)
axes3.set_ylim(numpy.min(min_data), numpy.max(min_data) * 1.1)
```

:::::::::::::::::::::::::


:::::::::::::::::::::::::::::::::::::::  challenge

## Make Your Own Plot

Create a plot showing the standard deviation (`numpy.std`)
of the activity data for each day across all mole-rats.

:::::::::::::::  solution

## Solution

```python
std_plot = matplotlib.pyplot.plot(numpy.std(data, axis=1))
matplotlib.pyplot.show()
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::  challenge

## Moving Plots Around

Modify the program to display the three plots on top of one another
instead of side by side.

:::::::::::::::  solution

## Solution

```python
import numpy
import matplotlib.pyplot

data = numpy.loadtxt(fname='../data/molerat_activity_v1.csv', delimiter=',')

# change figsize (swap width and height)
fig = matplotlib.pyplot.figure(figsize=(3.0, 10.0))

# change add_subplot (swap first two parameters)
axes1 = fig.add_subplot(3, 1, 1)
axes2 = fig.add_subplot(3, 1, 2)
axes3 = fig.add_subplot(3, 1, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=1))

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=1))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=1))

fig.tight_layout()

matplotlib.pyplot.show()
```

:::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::



:::::::::::::::::::::::::::::::::::::::: keypoints

- Use the `pyplot` module from the `matplotlib` library for creating simple visualizations.

::::::::::::::::::::::::::::::::::::::::::::::::::


