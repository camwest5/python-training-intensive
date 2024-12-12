---
title: Statistics
--- 

This session is aimed as an overview of how to perform some statistical modelling with Python. **It is a Python workshop, not a statistics workshop** - if you'd like to better understand the statistical models, or need help deciding what's best for you, please consult a statistics resource or contact a statistician.

In this session, we'll cover

- Descriptive statistics
  - Measures of central tendancy
  - Measures of variability
  - Measures of correlation
  
- Inferential statistics
  - Linear regressions
  - Calculating confidence intervals
  - T-tests
  - $\chi^2$ test
  - ANOVAs

We'll use three new modules:
 - `numpy`
 - `scipy.stats`
 - `statsmodels`

We'll be working from our "Players2024" dataset again. To bring it in and clean it up,

```python
import pandas as pd

df = pd.read_csv("Players2024.csv")
df = df[df["positions"] != "Missing"]
df = df[df["height_cm"] > 100]
```

## Descriptive Statistics

We'll start with sample size. All dataframes have most descriptive statistics functions available right off the bat which we access via the `.` operator. 

To calculate the number of non-empty observations in a column, say the numeric variable `df["height_cm"]`, we use the `.count()` method

```python
df["height_cm"].count()
```

### Measures of central tendancy
We can compute measures of central tendancy similarly. The average value is given by

```python
df["height_cm"].mean()
```

the median by

```python
df["height_cm"].median()
```

and the mode by

```python
df["height_cm"].mode()
```

> `.mode()` returns a dataframe with the most frequent values as there can be multiple.


### Measures of variance

We can also compute measures of variance. The minimum and maximum are as expected

```python
df["height_cm"].min()
df["height_cm"].max()
```

The range is the difference

```python
df["height_cm"].min() - df["height_cm"].max()
```

Quantiles are given by `.quantile(...)` with the fraction inside. The inter-quartile range (IQR) is the difference between 25% and 75%.

```python
q1 = df["height_cm"].quantile(0.25)
q3 = df["height_cm"].quantile(0.75)
IQR = q3 - q1
```

A column's standard deviation and variance are given by

```python
df["height_cm"].std()
df["height_cm"].var()
```

And the standard error of the mean (SEM) with

```python
df["height_cm"].sem()
```

You can calculate the skewness and kurtosis (variation of tails) of a sample with

```python
df["height_cm"].skew()
df["height_cm"].kurt()
```

All together, you can see a nice statistical summary with

```python
df["height_cm"].describe()
```

### Measures of correlation

If you've got two numeric variables, you might want to examine covariance and correlation. These indicate how strongly the variables are linearly related. We'll need to use the `df["Age"]` variable as well.

The covariance between "height_cm" and "Age" is

```python
df["height_cm"].cov(df["Age"])
```

> The `.cov()` function compares the column it's attached to (here `df["height_cm"]`) with the column you input (here `df["Age"]`). This means we could swap the columns without issue:
>
> ```python
> df["Age"].cov(df["height_cm"])
> ```

Similarly, we can find the Pearson correlation coefficient between two columns. 

```python
df["height_cm"].corr(df["Age"])
```

You can also specify "kendall" or "spearman" for their respective correlation coefficients

```python
df["height_cm"].corr(df["Age"], method = "kendall")
df["height_cm"].corr(df["Age"], method = "spearman")
```

### Reminder about groupbys

Before we move to inferential statistics, it's worth reiterating the power of groupbys discussed in the second workshop.

To group by a specific variable, like "positions", we use 

```python
gb = df.groupby("positions")
```

By applying our statistics to the `gb` object, we'll apply them to *every* variable for *each* position. Note that we should specify `numeric_only = True`, because these statistics won't work for non-numeric variables

```python
gb.mean(numeric_only = True)
```


## Inferential Statistics

Inferential statistics requires using the module `scipy.stats`, which we'll bring in with

```python
import scipy.stats as stats
```


### Simple linear regressions

Least-squares regression for two sets of measurements can be performed with the function `stats.linregress()`:

```python
stats.linregress(x = min_heights["Age"], y = df["height_cm"])
```

If we store this as a variable, we can access the different values with the `.` operator. For example, the p-value is

```python
lm = stats.linregress(x = df["Age"], y = df["height_cm"])
lm.pvalue
```

#### Plotting it

Naturally, you'd want to plot this. We'll need to use the overlaying techniques from the visualisation session. Let's import **seaborn** and **matplotlib**

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

Start by making a scatterplot of the data,

```python
sns.relplot(data = df, x = "Age", y = "height_cm")
```

Then, you'll need to plot the regression as a line. For reference,

$$ y = \text{slope}\times x + \text{intercept}$$

So
```python
sns.relplot(data = df, x = "Age", y = "height_cm")

x_lm = df["Age"]
y_lm = lm.slope*x_lm + lm.intercept
sns.lineplot(x = x_lm, y = y_lm, color = "r")
```

### $t$-tests

We can also perform $t$-tests with the `scipy.stats` module. Typically, this is performed to examine the statistical signficance of a difference between two samples' means. Let's examine whether that earlier groupby result for is accurate for heights, specifically, **are goalkeepers taller than non-goalkeepers?**

Let's start by separating the goalkeepers from the non-goalkeepers in two variables

```python
goalkeepers = df[df["positions"] == "Goalkeeper"]
non_goalkeepers = df[df["positions"] != "Goalkeeper"]
```

The $t$-test for the means of two independent samples is given by

```python
stats.ttest_ind(goalkeepers["height_cm"], non_goalkeepers["height_cm"])
```

Yielding a p-value of $8\times 10^{-247}\approx 0$, indicating that the null-hypothesis (*heights are the same*) is extremely unlikely.

### ANOVAs

What about the means of the other three? We could use an ANOVA to examine them. We use the `stats.f_oneway()` function for this. However, this requires us to send a list of samples in for each group, so we should separate the three positions. 

```python
defender = df[df["positions"] == "Defender"].height_cm
midfield = df[df["positions"] == "Midfield"].height_cm
attack = df[df["positions"] == "Attack"].height_cm
```

We can then perform the ANOVA on this list of samples

```python
stats.f_oneway(defender, midfield, attack)
```

With $p = 3\times10^{-84}$, it looks like their positions are not all independent of height.

### $\chi^2$ tests

$χ^2$ tests are useful for examining the relationship of categorical variables by comparing the frequencies of each. Often, you'd use this if you can make a contingency table.

We only have one useful categorical variable here, "positions" (the others have too many unique values), so we'll need to create another. Let's see if there's a relationship between players' positions and names with the letter "a".

Make a binary column for players with the letter "a" in their names. To do this, we need to apply a string method to *all* the columns in the dataframe as follows

```python
df["a_in_name"] = df["name"].str.contains("a")
```

Let's cross tabulate positions with this new column

```python
a_vs_pos = pd.crosstab(df["positions"],df["a_in_name"])
print(a_vs_pos)
```

The $χ^2$ test's job is to examine whether players' positions depend on the presence of "a" in their name. To evaluate it we need to send the contingency table in:

```python
stats.chi2_contingency(a_vs_pos)
```

### Logistic regressions


### Multiple linear regressions
