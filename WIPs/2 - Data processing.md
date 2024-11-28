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
df["deviation_from_mean"] = abs(df["column_x"] -  df["column_x"].mean())
```
where `abs(...)` takes the absolute value


Now that we have a clean dataset, we can expand it by calculating new interesting variables.

For example, we can first sum the three greenhouse gases (as they use the same unit), and then calculate how much CO<sub>2</sub>-equivalent is emitted per person. We can also add GDP per capita to the dataset.

For the total greenhouse gas emissions in CO<sub>2</sub>e:

``` python
df['co2e'] = df[['co2', 'methane', 'nitrous_oxide']].sum(axis=1)
```

The operation is done row-wise: we use `axis=1` to specify that we apply the function in the column axis.

You can confirm by looking at the data that the NA values are skipped when calculating the sum. The help page for this method mentions the `skipna` argument, which is set to `True` by default:

``` python
df.sum?
```

    skipna : bool, default True
        Exclude NA/null values when computing the result.

And then, for the CO<sub>2</sub>e per capita and the GDP per capita:

``` python
df['co2e_pc'] = df.co2e / df.population
df['gdp_pc'] = df.gdp / df.population
```

We now have three extra columns in our dataset.

## Merging tables

It is common to want to merge two datasets from two different sources. To do that, you will need common data to match rows on.

We want to add the countries' Social Progress Index to our dataset.

> You can find out more about the SPI on their website: <https://www.socialprogress.org/>

The SPI dataset also has a three-letter code for the countries, which we can match to our existing `iso_code` column. We have an SPI for several different years, so we should match that column as well:

``` python
# read the data
spi = pd.read_csv('https://gist.githubusercontent.com/stragu/57b0a0750678bada09625d429a0f806b/raw/a18a454d7d225bd24074399a7ab79a4189e53501/spi.csv')
# merge on two columns
df_all = pd.merge(df, spi,
                  left_on=['iso_code', 'year'],
                  right_on=['country_code', 'year'])
```

We specified the two data frames, and which columns we wanted to merge on. However, we end up losing a lot of data. Looking at the documentation for the `merge()` function, we can see that there are many ways to merge tables, depending on what we want to keep:

``` python
pd.merge?
```

The `how` argument defines which kind of merge we want to do. Because we want to keep all of the data from `df`, we want to do a "left merge":

``` python
df_all = pd.merge(df, spi,
                  how='left',
                  left_on=['iso_code', 'year'],
                  right_on=['country_code', 'year'])
```

We can now "drop" the useless country_code column:

``` python
df_all.pop('country_code')
```

> Notice that the `pop` method is an "in-place" method: you don't need to reassign the variable.

## Summaries

The `aggregate()` method, which has a shorter alias `agg()`, allows creating summaries by applying a function to a column. In combination with the `groupby()` method, we can create summary tables. For example, to find the average SPI for each country, and then sort the values in descending order:

``` python
df_all.groupby('country').spi.agg('mean').sort_values(ascending=False)
```

If you want to export that summary table and use it outside Spyder, you can first save it as a variable, and then write it to a CSV file:

``` python
spi_sum = df_all.groupby('country').spi.agg('mean').sort_values(ascending=False)
# write to file
spi_sum.to_csv('spi_summary.csv')
```

> The CSV file should be found in your project directory, as it became the default working directory when we created the project.

## Visualising data

pandas integrates visualisation tools, thanks to the `plot()` method and its many arguments.

For example, to visualise the relationship between CO<sub>2</sub>e per capita and SPI:

``` python
df_all.plot(x='co2e_pc', y='spi')
```

The default kind of plot is a line plot, so let's change that to a scatterplot:

``` python
df_all.plot(x='co2e_pc', y='spi', kind='scatter')
```

Focusing on the latest year will guarantee that there only is one point per country:

``` python
df_all[df_all.year == 2016].plot(x='co2e_pc',
                                 y='spi',
                                 kind='scatter')
```

To visualise a third variable, GDP per capita, let's map it to the colour of the points, thanks to the `c` argument:

``` python
df_all[df_all.year == 2016].plot(x='co2e_pc',
                                 y='spi',
                                 c='gdp_pc',
                                 colormap='viridis',
                                 kind='scatter')
```

We can change the labels too:

``` python
df_all[df_all.year == 2016].plot(x='co2e_pc',
                                 y='spi',
                                 c='gdp_pc',
                                 colormap='viridis',
                                 kind='scatter',
                                 xlabel='GHG per capita (MT CO2e/yr)',
                                 ylabel='Social Progress Index')
```

If the x labels don't show, try this workaround: <https://github.com/pandas-dev/pandas/issues/36064#issuecomment-1011175535>

### Challenge 2: GHG timeline

How would you visualise global GHG emissions over the years, with one line per type of GHG?

We can subset the columns that matter to us, create a summary, and plot it:

``` python
sub = df_all[['year', 'co2', 'methane', 'nitrous_oxide']]
sub.groupby('year').agg('sum').plot(ylabel='MT CO2e')
```

Remember that the default `kind` of plot in this function is `'line'`, which works for this visualisation. And as we fed it a series variable with several columns, it automatically assigned a different colour to each one.

## Saving your work

Your project can be reopened from the "Projects" menu in Spyder.

By default, your variables are *not* saved, which is another reason why working with a script is important: you can execute the whole script in one go to get everything back. You can however save your variables as a `.spydata` file if you want to (for example, if it takes a lot of time to process your data).

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
-   About our datasets:
    -   [Our World in Data](https://ourworldindata.org)
    -   [Social Progress Index](https://www.socialprogress.org)
-   Our [compilation of useful Python links](https://github.com/uqlibrary/technology-training/blob/master/Python/useful_links.md)