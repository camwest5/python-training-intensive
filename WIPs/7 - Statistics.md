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

## Inferential Statistics

Inferential statistics requires using the module `scipy.stats`, which we'll bring in with

```python
import scipy.stats as stats
```

### Simple linear regressions

### Multiple linear regressions

### Confidence intervals

### T-tests

### $\chi^2$ tests

### ANOVAs
