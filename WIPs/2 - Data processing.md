---
title: Data Processing
--- 

In this second workshop we will cover

- Examining / exploring data
- Filtering rows and columns
- Basic descriptive statistics
- Adding new columns
- Group bys and summary tables

This hands-on course -- directed at intermediate users -- looks at using the **pandas** module to transform and visualise tabular data.

## Setting up
### Introducing pandas

Pandas is a Python module that introduces dataframes to Python. It gives us the tools we need to clean and transform data with Python.

To be able to use the functions included in pandas, we have to first import it:

``` python
import pandas as pd
```

`pd` is the usual nickname for the pandas module.

> If you get an error, like `No module named 'pandas'`, you'll need to install it first, using either `conda install pandas` or `pip install pandas`, depending on your Python installation.

#### The DataFrame object

Pandas is built upon one key feature: the DataFrame class. In Python we have different built-in types, like `int` for integers and `string` for characters. Pandas introduces a new type, `DataFrame`, which stores data like a spreadsheet.

### Setting up the workspace

To make life easy, we should set up our workspace well. 

1. Open your project folder using your file explorer, and create a new folder called "data". 
2. Move your data into this folder.
3. Next, open your project in Spyder, and create a new script called "analysis.py".
4. Open the "Files" tab in Spyder and check that you see two objects:
   * The file "analysis.py"
   * The folder "data"
 
### Importing data

Pandas offers a simple way to access data with its `read.csv()` function. We'll save it into the variable `df_raw`:

``` python
df_raw = pd.read_csv("data/name_of_file_here.csv")
```

> You can also provide a URL instead of a file path!

### Aside - File Paths and backslashes
Just a quick detour to discuss file paths of which there are two types: **absolute** and **relative**

#### Absolute

Absolute file paths always start at the "top" of your file system, e.g. one of the drives (like C:) for Windows users, so they are never ambiguous. It's like providing your full address from country to street number.

```bash
C://Users/my_username/research/data/really_important_secret_data.csv
```

#### Relative

Relative file paths start from **your current file location**. For files in my current folder, I just provide their name - like referring to another house on your street as "number 7". **Let's assume we're in the research folder**.

```bash
file_in_my_current_folder.csv
```

We can go to *down* folders from our current location:

```bash
data/really_important_secret_data.csv
```

And we can go *up* folders from our current location
```bash
../../this_file_is_two_levels_up.csv
```

Or a combination of the two (e.g. up one, then down into a *different* folder)
```bash
../not_research/this_file_is_not_research.csv
```

**What matters is that the relative reference depends on where your code is and will break if you move the script!**


#### Backslashes

One last note: Windows uses backslashes for their file paths
```bash
C:\\Users\...
```
But Python uses backslashes as an escape character. For example, `"\n"` is a newline, `"\u1234"` is the unicode character U+1234 and confusingly `"\\"` is a **single** backslash. So we have to modify all Windows file paths to either
```bash
C:\\\\Users\\...

OR

C://Users/...
```
You can choose whichever you prefer.

### Initial look at the data

Let's get back to data.

We can investigate the size of the data thanks to the `shape` attribute attached to all pandas dataframes:

``` python
df_raw.shape
```

The dataset contains dozens of columns. What are their names?

``` python
df_raw.columns
```

Let's subset our data to focus on a handful of variables.

### Creating a backup

Data analysis in Python is safe because our variables are *copies* of the data - we aren't actually changing the files until we explicitly overwrite them. However, Python also has no *undo*, so if I delete something in my analysis, I can't get it back - I have to start all over again.

One way to mitigate this issue is by making a copy of the data

```python
df = df_raw.copy()
```

Now we have two variables: `df` is what we'll use, and `df_raw` stores the raw data. If we ever need to restart, we can simply run `df = df_raw.copy()`.

## Accessing and Filtering Data

So how do we access our data in Python? We use a type of indexing introduced by pandas, which revolves around using square brackets after the dataframe: `df[...]`.

### Accessing columns
To access a column, index with its name:

```python
df["column_name"]
```

We can access multiple by providing a **list** of names
```python
# Save the names in a list and then index
column_names = ["name_1", "name_2"]
df[column_names]

# This is equivalent to
df[["name_1", "name_2"]]
```

If we want to *do* anything with it (like statistics or visualisation), it's worth saving the column(s) as a new variable

```python
df_subset = df[["name_1", "name_2"]]
```

### Accessing rows
There's a few ways to access rows. The easiest is by slicing - if you want rows 5 to 10, use `df[5 : 10]`

> Note that the end row is **not included**

``` python
df[start_row : end_row]
```

If you want to access a single row, we need to use `df.loc[]` or `df.iloc[]`. These are the go-to methods for accessing data if the above indexing isn't sufficient.

* `df.loc[]` accesses rows by label (defaults to row number but could be anything)
* `df.iloc[]` accesses rows by row number exclusively

For a single row
```python
df.loc[row_label]
df.iloc[row_num]
```

Finally, we can filter specific rows **by a condition** on one of the variables, e.g. *only rows where variable $x > 15$*.

```python
df[df["column_x"] > 15]
# Or any other condition
```

As with the column case, it's useful to save this as a variable
```python
df_filtered = df[df["column_x"] > 15]
```

## Basic statistics

How might we perform some basic statistics on our data?

To check what kind of data each column is stored as, we can use the `dtypes` attribute:

``` python
df.dtypes
```

> In general, pandas will bring in numbers with `float64` and non-numeric data with `object`.

The `describe()` method is useful for descriptive statistics about our numerical columns:

``` python
df.describe()
```

However, it will only show the two first ones and two last ones. We can focus on a specific column instead, for example one that was hidden previously:

``` python
df["column"].describe()
```

Or a categorical column:

``` python
df["categorical_column"].describe()
```

> For a categorical column, the information shown is different: for example, how many unique values there are, and what the most common value is.

What if you want specific statistics about a particular column? Usually there are methods available:

```python
# Applicable to all columns
df["column"].count()
df["column"].unique()

# For numeric columns only
df["numeric_column"].min()
df["numeric_column"].max()
df["numeric_column"].mean()
df["numeric_column"].median()
df["numeric_column"].std()
# ...
```

We can use these methods to filter our data. For example, the row which has the maximum value of variable $x$ is
```python
x_max = df["variable_x"].max()
df[df["variable_x"] == x_max]

# Or in one line
df[df["variable_x"] == df["variable_x"].max()]
```
because we are looking for the row in `df["variable_x"]` (the whole column) that has the value `df["variable_x"].max()`.


## Challenge
**Reduce your dataset to $\le 5$ variables (columns) and $\le 100$ rows using conditions** by filtering down to a particular subset of your data.

## Adding and removing columns
Sometimes we need to add new columns. It's the same process as overwriting existing columns - let's make a new column called "zeroes" where every row is 0

```python
df["zeroes"] = 0
```

We can also send in a column, for example
```python
df["copy_of_x"] = df["column_x"]
```

Perhaps most usefully, we can manipulate the column we send in. For example, the deviation from the mean
$$|\bar{x} - x_i|$$
can be computed for each row:
```python
col_x = df["column_x"]
avg_x = df["column_x"].mean()

df["deviation_from_mean"] = abs(col_x - avg_x)

# Or all together on one line,
df["deviation_from_mean"] = abs(df["column_x"] - df["column_x"].mean())
```
where `abs(...)` takes the absolute value

Notice that we subtracted a value from a column. We can also perform mathematics with multiple columns:
```python
df["product"] = df["column_x"]*df["column_y"]
```

Let's remove these new columns that we don't need with the method `df.drop(columns = [...])`:

```python
df.drop(columns = ["zeroes", "copy_of_x", "deviation_from_mean", "product"])
```

## Summaries

After cleaning up our data, we need to analyse it. This usually involves some kind of aggregation. For example, *what is the average $x$ per year?* requires aggregating over variable $x$ for each year. 

First, we need to group by a specific variable

```python
gb = df.groupby("year")
```

This thing in itself is a pretty abstract Python object, best thought of as a dataframe where we've identified a grouping variable.

Next, we need to apply some aggregation to it (the groupby tells it to do it for each year)

```python
avg_x_per_year = gb["variable_x"].agg("mean")
```

Of course, we could have done this in one line:
```python
avg_x_per_year = df.groupby("year").agg("mean")
```

This is a really useful tool, because now we have something we can *visualise*. As the next session will show us, the visualisation tools generally just take in numbers and turn them into dots. We need to do the stats *beforehand*.

As a taster, try running
```python
avg_x_per_year.plot()
```

## Exporting results

The last step in the process is saving the data. Let's say we want to take that final dataframe and export it to a csv. That's what the `df.to_csv()` method is for

```python
avg_x_per_year.to_csv("data/avg_x_per_year.csv")
```

This will save the dataframe to a .csv file and place it in the data folder.

## Resources

-   [Official pandas documentation](https://pandas.pydata.org/)
    -   [Getting started](https://pandas.pydata.org/docs/getting_started/index.html)
    -   [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
    -   [User guide](https://pandas.pydata.org/docs/user_guide/index.html)
-   More visualisation modules:
    -   [Altair](https://altair-viz.github.io/)
    -   [Bokeh](https://docs.bokeh.org/en/latest/)
    -   [Vega](https://vega.github.io/vega/)
    -   [Matplotlib](https://matplotlib.org/)
-   Our [compilation of useful Python links](https://github.com/uqlibrary/technology-training/blob/master/Python/useful_links.md)