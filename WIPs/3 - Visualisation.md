# Visualisation

In this second workshop we will cover

- Simple visualisations with seaborn
- Making modifications with matplotlib
- Matplotlib from scratch
- Interactive visualisations with plotly

See analysis.py for seaborn stuff.


## Setting up
With the data manipulation tools from pandas, we can now visualise our data. For this workshop we'll be working from the "Players2024.csv" dataset, which we should bring in with pandas:

```python
import pandas as pd
df = pd.read_csv("data/Players2024.csv")
```

Take a quick peak at the dataset to remind yourself
```python
print(df)
```

## Seaborn for simple visualisations
To begin our visualisations, we'll use the package [seaborn]((https://seaborn.pydata.org/index.html)), which allows you to quickly whip up decent graphs. 

```python
import seaborn as sns
```

> It's called "seaborn" as a reference to fictional character [Sam Seaborn](https://en.wikipedia.org/wiki/Sam_Seaborn), whose initials are "sns".

Seaborn has three plotting functions
```python
sns.catplot(...) # for categorical plotting, e.g. bar plots, box plots etc.
sns.relplot(...) # for relational plotting, e.g. line plots, scatter plots
sns.displot(...) # for distributions, e.g. histograms
```
We'll begin with the first.

### Categorical plots
Categorical plots are produced with seaborn's `sns.catplot()` function. There are two key pieces of information to pass:

* The data
* The variables

Let's see if there's a relationship between the players' **heights** and **positions**, by placing their positions on the $x$ axis and heights on the $y$. 


```python
sns.catplot(data = df, x = "positions", y = "height_cm")
```
Our first graph! This is called a *swarm* plot; it's like a scatter plot for categorical variables.

It's already revealed two things to us about the data:

* There are some incorrect heights - nobody is shorter than 25cm!
* Someone's position is "missing"

Let's get rid of these with the data analysis techniques from last session

```python
# Remove missing position
df = df[df["positions"] != "Missing"]

# Ensure reasonable heights
df = df[df["height_cm"] > 100]
```

Run the plot again, it's more reasonable now
```python
sns.catplot(data = df, x = "positions", y = "height_cm")
```

#### Bar plots

Swarm plots are interesting but not standard. You can change the plot type with the `kind` parameter

```python
sns.catplot(data = df, x = "positions", y = "height_cm", kind = "bar")
```

> Many aspects of your plot can be adjusted by sending in additional parameters and is where seaborn excels.

It seems like goalkeepers are taller, but not by much. Let's look at the standard deviation for each position by changing the `estimator = ` parameter (default is mean)

```python
sns.catplot(data = df, x = "positions", y = "height_cm", kind = "bar", estimator = "std")
```

Clearly there's a lot less variation in goalkeepers - they're all tall.

#### Box plots

Let's make box plots instead. It's the same procedure, just change to `kind = "box"` and remove `estimator = `

```python
sns.catplot(data = df, x = "positions", y = "height_cm", kind = "box")
```

Just as we predicted.

### Distributions

#### Histograms
Let's move to the "Age" parameter now. We can look at the distribution of ages with

```python
sns.displot(data = df, x = "Age")
```

Looks a bit funny with those gaps - let's change the number of bins with `bins = 28`

```python
sns.displot(data = df, x = "Age", bins = 28)
```

Now, what if you wanted to look at the distribution for different variables? We can make a separate distribution for each position with the `col = "position"` argument, specifying a new column for each position

```python
sns.displot(data = df, x = "Age", bins = 28, col = "positions")
```

#### Kernel density estimates
Finally, you don't *have* to do histograms. You could also do a Kernel Density Estimate, with `kind = "kde"` (let's remove `bins = ` and `col = `)

```python
sns.displot(data = df, x = "Age", kind = "kde")
```

If you want a separate line for each position, we should indicate that each position needs a different colour/hue with `hue = "position"`
```python
sns.displot(data = df, x = "Age", hue = "position", kind = "kde")
```

### Relational plots

It seems like players peak in their mid-twenties, but goalkeepers stay for longer. Let's see if there's a relationship between players' **age** and **height**

#### Scatter plots

We'll start with a scatter plot

```python
sns.relplot(data = df, x = "Age", y = "height_cm")
```

Not much of a trend there, although the bottom-right looks a bit emptier than the rest (could it be that short old players are the first to retire?).

We can use `hue = ` to have a look at positions again

```python
sns.relplot(data = df, x = "Age", y = "height_cm", hue = "positions")
```

Yup, goalkeepers are tall, and everyone else is a jumble.

#### Line plots

Let's do a line plot of the average height per age.

```python
sns.relplot(data = df, x = "Age", y = "height_cm", kind = "line")
```

Seems pretty flat, except the ends are a bit weird because there's not much data. Let's eliminate everything before 17 and after 35 and plot it

```python
# Create smaller dataframe
condition = (df["Age"] > 17) & (df["Age"] < 35)
inner_ages = df[condition]

# Line plot
sns.relplot(data = inner_ages, x = "Age", y = "height_cm", kind = "line")
```

Looks a bit shaky but that's just because it's zoomed in - notice that we go from 182cm to 184cm. We'll fix this when we look at matplotlib in the next section.

#### Combining the two

We can combine our scatter and line plots together.

1. Make the first plot as normal
2. For all additional (overlaying) plots, use an **axes-level plot** instead of `sns.relplot()` etc. These just draw the points/bars/lines, and are normally behind-the-scenes. There's one for every plot type, and look like
    * `sns.lineplot()`
    * `sns.scatterplot()`
    * `sns.boxplot()`
    * `sns.histplot()`
    * etc.

For example,
```python
# Figure level plot
sns.relplot(data = df, x = "Age", y = "height_cm", hue = "positions")

# Axes level plot (drop the kind = )
sns.lineplot(data = inner_ages, x = "Age", y = "height_cm")
```
> **You can't include `kind = ` inside an axes level plot**

Let's swap the colour variable from the scatter plot to the line plot
```python
# Figure level plot
sns.relplot(data = df, x = "Age", y = "height_cm")

# Axes level plot (drop the kind = )
sns.lineplot(data = inner_ages, x = "Age", y = "height_cm", hue = "positions")
```

Finally, let's make the scatter dots smaller with `s = 10` and grey with `color = "grey"`.
```python
# Figure level plot
sns.relplot(data = df, x = "Age", y = "height_cm", s = 10, c = "grey")

# Axes level plot (drop the kind = )
sns.lineplot(data = inner_ages, x = "Age", y = "height_cm", hue = "positions")
```

## Going deeper with matplotlib


## Interactivity with plotly