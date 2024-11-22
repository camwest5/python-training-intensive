# Fundamentals

In this first workshop we will cover

- Variables
- Functions
- Modules
- Importing data

## Introducing Python and Spyder

Python is a **programming language** that can be used to build programs (i.e. a "general programming language"), but it can also be used to analyse data by importing a number of useful modules.

We are using **Spyder** to interact with Python more comfortably. If you have used RStudio to interact with R before, you should feel right at home: Spyder is a program designed for doing data science with Python.

Python can be used **interactively** in a console, or we can build **scripts and programs** with it, making the most out of Spyder's code editor.

We will start by using the **console** to work interactively. This is
our direct line to the computer, and is the simplest way to run code.
Don’t worry about any unfamiliar language, fonts or colours - we can
ignore most of it for now - all you need to know is that

- `In [1]: ...` is code that we’ve sent to the computer, and
- `Out[1]: ...` is its response.

## Operators

To start with, we can use Python like a calculator. Type the following **commands** in the console, and press <kbd>Enter</kbd> to **execute** them:

### Maths

To start with, we can use Python like a calculator. Type the following
**commands** in the console, and press <kbd>Enter</kbd> to **execute**
them:

``` python
1 + 1
```

```python
2 * 3
```

```python
4 / 10
```

```python
5 ** 2
```

After running each command, you should see the result as an output.

## Variables

Like language, Python has nouns and verbs. We call the nouns **variables**: they are the 'things' we manipulate with our code.

Essentially, a variable is a named container. We access it by its **name**, and we get its **value**.

To create a variable, you need to choose a name and a value with `name = value`. For example

```python
example_int = 42
```

Whenever you use the variable's name, Python will now access its value:

```python
example_int
```

We can use the variables in place of the values

```python
example_float = 5.678
product = example_int * example_float
product
```

> Spyder helps us with extra panels and features apart from the Console. To see what variables you have created, look at the "Variable explorer" tab in the top right.

### Types

Variables have different types. So far, we've just looked at storing numbers, of which there are three types:

- `int` - integers store whole numbers, e.g. `1, 5, 1000, -3`.
- `float` - floating point numbers store decimals and scientific notation, e.g. `1.5, -8.97, 4e-6`.
- `complex` - complex numbers express the imaginary unit with `j`, e.g. `z = 1+2j` is $z = 1+2i$.

Let's look at some other types

#### Booleans

Even simpler than integers is the **boolean** type. These are either 1
or 0 (True or False), representing a single binary unit (bit). Don’t be
fooled by the words, these work like numbers: `True + True` gives `2`.

``` python
example_bool = True
```

> In Python, the boolean values `True` and `False` **must** begin with a
> capital letter.

#### Strings

Let’s look at variable types which aren’t (necessarily) numbers.
**Sequences** are variables which store multiple pieces of data. For
example, **strings** store a sequence of characters and are created with
quotation marks `'blah blah blah'` or `"blah blah blah"`:

``` python
example_string = 'This is an example of a string!'
```

#### Lists

We can also create **lists**, which will store several variables (not
necessarily of the same type). We need to use square brackets for that:

``` python
example_numbers = [38, 3, 54, 17, 7]
example_diverse = [3, 'Hi!', 9.0]
```

Lists are very flexible as they can contain any number of items, and any
type of data. You can even nest lists inside a list, which makes for a
very flexible data type.

Operations on sequences are a bit different to numbers. We can still use
`+` and `*`, but they will concatenate (append) and duplicate, rather
than perform arithmetic.

``` python
example_string + ' How are you?'
example_numbers + example_diverse
3 * example_numbers
```

However, depending on the variable, some operations won’t work:

``` python
sentence + favNumber
```

There are other data types like tuples, dictionaries and sets, but we
won’t look at those in this session. Here’s a summary of the ones we’ve
covered:

| Category | Type | Short name | Example | Generator |
|----|----|----|----|----|
| Numeric | Integer | `int` | `3` | `int()` |
| Numeric | Floating Point Number | `float` | `4.2` | `float()` |
| Numeric | Boolean | `bool` | `True` | `bool()` |
| Sequence | String | `str` | `'A sentence '` | `" "` or `' '` or `str()` |
| Sequence | List | `list` | `['apple', 'banana', 'cherry']` | `[ ]` or `list()` |

The **generator** commands are new. We use these to manually change the
variable type. For example,

``` python
int(True)
```


yields `1`, converting a **boolean** into an **integer**. These commands
are **functions**, as opposed to variables - we’ll look at functions a
bit later.

### Indexing

We can access part of a sequence by **indexing**. Sequences are ordered,
**starting at 0**, so the first element has index 0, the second index 1,
the third 2 and so on. For example, see what these commands return:

``` python
example_string[0]
example_string[6]
example_numbers[4]
```

If you want more than one element in a sequence, you can **slice**.
Simple slices specify a range to slice, from the first index to the
last, **but not including the last**. For example:

``` python
myList[0:4]
```

That command returns elements from position 0 up to - but not
including! - position 4.

## Scripts

So far, we’ve been working in the console, our direct line to the
computer. However, it is often more convenient to use a **script**.
These are simple text files which store code and run when we choose.
They are useful to

- write code more comfortably,
- store clearly defined steps in chronological order,
- share a process with peers easily, and
- make your work reproducible

Let’s create a folder system to store our script in by creating a
**project**.

- Press `Projects > New project...` and name your project,
perhaps “python_training”. 
- Create a new script with
<kbd>ctrl</kbd>+<kbd>N</kbd>, `File > New file...` or the new file
button.

You should now see a script on the left panel in Spyder, looking
something like this:

Try typing a line of code in your new script, such as

``` python
example_message = "This is an example message"
example_message
```

Press <kbd>F9</kbd> to run each line, or
<kbd>ctrl</kbd>+<kbd>enter</kbd> for the whole script. You should see
something like the following appear in the **console** (depending on how
you ran it):


We’ll work out of a script for the rest of the session. Don’t forget to
save your script by pressing <kbd>ctrl</kbd>+<kbd>S</kbd> or the save
button.
)

## Functions

**Functions** are little programs that do specific jobs. These are the
verbs of Python, because they do things to and with our variables. Here
are a few examples of built-in functions:

``` python
len(myList)
min(myList)
max(myList)
sum(myList)
round(otherNumber)
```

Functions always have parentheses () after their name, and they can take
one or several **arguments**, or none at all, depending on what they can
do, and how the user wants to use them.

Here, we use two arguments to modify the default behaviour of the
`round()` function:

``` python
round(otherNumber, 2)
```

    5.68

> Notice how Spyder gives you hints about the available arguments after
> typing the function name?

### Operators

Operators are a special type of function in Python with which you’re
already familiar. The most important is `=`, which assigns values to
variables. Here is a summary of some important operators, although there
are many others:

#### General

| Operator | Function | Description | Example command |
|----|----|----|----|
| = | Assignment | Assigns values to variables | `a = 7` |
| \# | Comment | Excludes any following text from being run | `# This text will be ignored by Python` |

#### Mathematical

| Operator | Function | Description | Example command | Example output |
|----|----|----|----|----|
| \+ | Addition | Adds or concatenates values, depending on variable types | `7 + 3` or `"a" + "b"` | `10` or `'ab'` |
| \- | Subtraction | Subtracts numerical values | `8 - 3` | `5` |
| \* | Multiplication | Multiplies values, depending on variable types | `7 * 2` or `"a" * 3` | `14` or `'aaa'` |
| / | Division | Divides numerical vlues | `3 / 4` | `0.75` |
| \*\* | Exponentiation | Raises a numerical value to a power | `7 ** 2` | `49` |
| % | Remainder | Takes the remainder of numerical values | `13 % 7` | `6` |

#### Comparison

| Operator | Function | Description | Example command | Example output |
|----|----|----|----|----|
| == | Equal to | Checks whether two variables are the same and outputs a boolean | `1 == 1` | `True` |
| != | Not equal to | Checks whether two variables are different | `'1' != 1` | `True` |
| \> | Greater than | Checks whether one variable is greater than the other | `1 > 1` | `False` |
| \>= | Greater than or equal to | Checks whether greater than (\>) or equal to (==) are true | `1 >= 1` | `True` |
| \< | Less than | Checks whether one variable is less than the other | `0 < 1` | `True` |
| \<= | Less than or equal to | Checks whether less than (\<) or equal to (==) are true | `0 <= 1` | `True` |

## Finding help

To find help about a function, you can use the `help()` function, or a
`?` after a function name:

``` python
help(max)
print?
```

    Help on built-in function max in module builtins:

    max(...)
        max(iterable, *[, default=obj, key=func]) -> value
        max(arg1, arg2, *args, *[, key=func]) -> value

        With a single iterable argument, return its biggest item. The
        default keyword-only argument specifies an object to return if
        the provided iterable is empty.
        With two or more arguments, return the largest argument.

In Spyder, you can use the <kbd>Ctrl</kbd> + <kbd>I</kbd> keyboard
shortcut to open the help in a separate pane.

> The help information can often be dense and difficult to read at
> first, taking some practice. In the [next
> session](https://github.com/uqlibrary/technology-training/blob/4ea3e86ab8f6f43a73c3b3a44d63a00ac8d366f8/Python/revamp/data_transformation.md)
> we look closer at interpreting this **documentation**, one of the most
> important Python skills.

For a comprehensive manual, go to the [official online
documentation](https://docs.python.org/). For questions and answers,
typing the right question in a search engine will usually lead you to
something helpful. If you can’t find an answer, [StackOverflow is a
great Q&A community](https://stackoverflow.com/questions/tagged/python).

## Modules

To do more with Python, you could write new functions from scratch, but it is easier to import extra **modules** to extend its capabilities. For example, to access the `pi` constant:

```python
pi # throws an error: it does not exist!
import math # this module contains the pi constant
math.pi # we have to specify where it comes from
import math as m # give a shorter name
m.pi
from math import pi # only import what is necessary
pi
```

`math` is part of the "Python standard library". You can see all the functions and constants available in the `math` module here: https://docs.python.org/3/library/math.html

Python distributions like Anaconda already come with a number of useful extra modules for science.

### Installing extra modules

To install more modules, you might need to use `pip` (on most systems) or `conda` (if you use Anaconda or Miniconda) from the command line.

With `pip`, which will fetch the module from the [Python Package Index](https://pypi.org/) (PyPI):

```bash
pip install some-module
```

With `conda`, which will fetch the module from the Anaconda repository:

```bash
conda install some-module
```

Refer to the module's website to find what is recommended.

Here, we present a few modules that are very important for data science with Python, and which are already available in the Anaconda distribution.

### NumPy for arrays

Arrays are a data type introduced by `numpy`, a module with many functions useful for numerical computing.

For example, you can convert the list we created before to then do mathematical operations on each one of its elements:

```python
import numpy as np
myArray = np.array(myList)
myArray * 2
```

### Pandas for dataframes

`pandas` introduces dataframes, which are often used to store two-dimensional datasets with different kinds of variables in each column. If your data is stored as a spreadsheet, you probably want to import it with a pandas function.

Here is an example of creating a pandas dataframe from scratch, populating it by hand:

```python
import pandas as pd
df = pd.DataFrame(columns=['Name', 'Age'])
# populate the dataframe:
df.loc[1] = 'Josephine', 70
df.loc[2] = 'Dilsah', 38
df
df.Age # access a specific variable
```

> You can double-click on a dataframe in the Variable explorer to explore it in a separate window.

### Matplotlib for visualisation

`matplotlib` is a large collection of data visualisation functions, and `pyplot` is a submodule of `matplotlib` that contains essentials.

```python
import matplotlib.pyplot as plt
plt.plot(myList)
```

This shows a plot in the Plots tab of Spyder.

> In a Python shell, you might have to use the `plt.show()` command to show the plot.

The default look is a line plot that joins all the points, but we can style a plot with only a few characters:

```python
# blue circles
plt.plot(myList, 'bo')
# green squares, dashed line:
plt.plot(myList, 'gs--')
```

Extra arguments can be used to style further:

```python
# red, diamonds, solid line; change width of line and size of diamonds:
plt.plot(myList, 'rd-', linewidth=3, markersize=10)
```

To find out about the styling shorthand and all other arguments, look at the documentation:

```python
plt.plot?
```

<!-- 
## Example project

A project is useful to keep everything related to one job all contained in one directory.

### Create a new project

Create a project with `Projects > New project...`. You can name this one "python_intro" for example.

### Create a script

A script is a simple text file that contains code. It is useful to:

* write code more comfortably
* store clearly defined steps in a chronological order
* share a process with peers easily
* make your work reproducible

Click on  the "New file" icon, and save it as "process.py" in your project directory.

Remember to add comments (they start with the `#` symbol) to document your work: this will be useful if you share your work with others, or even for your future self!

To execute something from the script (the current line, or a selected block), use the <kbd>F9</kbd> keyboard shortcut (or the white "Run" button).

### Import data

It is possible to **read a CSV file with a `pandas` function**.

#### Challenge 1: Import data

Have a look at the documentation for the `read_csv()` function:

```python
import pandas as pd
pd.read_csv?
```

How could you use it to store the following dataset into a variable?

https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv

#### Solution

We have to create a variable, and store the output of the function inside it. No need to download the file first: `read_csv()` can read from a URL!

```python
gap = pd.read_csv('https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv')
```

> `pandas` contains many functions for interpreting a variety of file formats. Start typing `pd.read_` to see what is available.

Now that we have stored our dataset as a variable, we can print the dataset to the console:

```python
gap
```

The console conveniently shows us only the beginning and end of the dataframe.

We can also use the "dot notation" to create commands that are useful to explore the data:

```python
gap.shape # size of the dataframe (an attribute)
gap.head() # first few rows (a method)
gap.head(10) # change the behaviour of the method
gap.tail() # last few rows
gap.country # single variable
```

Variables have **attributes** and **methods** attached to them, depending on the data type. Here, `shape` is an attribute, i.e. a static characteristic of the variable, whereas `head()` is a method, i.e. a function that can often take arguments.

### Analyse data

Let's now learn a bit more about our data. The `describe()` method gives us summary statistics for our numerical data:

```python
gap.describe()
```

To create a customised summary, we can string different methods one after the other. Here, we first group by year to then get the yearly mean of the numerical columns, using `True` to indicate that we only want to consider the numeric columns:

```python
gap.groupby('year').mean(True)
```

### Visualise data

We can visualise our data with `matplotlib`. First, let's visualise the relationship between gross domestic product per capita (`gdpPercap`) and life expectancy (`lifeExp`) with a scatterplot:

```python
import matplotlib.pyplot as plt
plt.plot(gap.gdpPercap, gap.lifeExp, 'g.')
```

We add the data as two arguments, which are understood as what we put on the x and y axes respectively.

We can now add labels with extra functions:

```python
plt.plot(gap.gdpPercap, gap.lifeExp, 'g.')
plt.xlabel('GDP per capita (USD)')
plt.ylabel('Life expectancy (years)')
```

> Make sure that you execute all the lines of code that relate to one plot *together*. When you need to execute many lines together, you might want to start using **cells** in your script: you can start a new cell with a `#%%` line, and execute the current cell with the keyboard shortcut <kbd>Ctrl</kbd> + <kbd>Enter</kbd>.

#### Saving plots

You can save you plots as PNG by right-clicking on them. To save automatically with some code, you can add the following line to the visualisation block:

```python
plt.savefig('gdp_vs_life_exp.pdf')
```

A PDF is a great option for a visualisation in vector format.

You can change the extension in the filename to save in a different format. For example, for a PNG file with a higher definition than the default:

```python
plt.savefig('gdp_vs_life_exp.png', dpi=600)
```

#### Challenge 2: Visualise mean life expectancy over the years

1. How can we reuse previous code to visualise how mean life expectancy evolved over the years?
1. Try changing the look of the plot to a magenta dotted line.

#### Solution

We can reuse the same summary as before, but adding the attribute of the right column we are interested in:

```python
plt.plot(gap.groupby('year').mean().lifeExp, 'm:')
``` -->

## Saving your work

Press "Save" or <kbd>Ctrl</kbd> + <kbd>S</kbd> to save your script.

Your project can be reopened from the "Projects" menu in Spyder.

By default, your variables are *not* saved, which is another reason why working with a script is important: you can execute the whole script in one go to get everything back. You can however save your variables as a `.spydata` file if you want to (for example, if it takes a lot of time to process your data).

## Summary

This morning we looked at a lot of Python features, so don’t worry if they
haven’t all sunk in. Programming is best learned through practice, so
keep at it! Here’s a rundown of the concepts we covered

| Concept | Desctiption |
|----|----|
| **The console vs scripts** | The **console** is our window into the computer, this is where we send code directly to the computer. **Scripts** are files which we can write, edit, store and run code, that’s where you’ll write most of your Python. |
| **Variables** | **Variables** are the nouns of programming, this is where we store information, the objects and things of our coding. They come in different types like integers, strings and lists. |
| **Indexing** | In order to access elements of a sequence variable, like a list, we need to **index**, e.g. `myList[2]`. Python counts from 0. |
| **Functions** | **Functions** are the verbs of programming, they perform actions on our variables. Call the function by name and put inputs inside parentheses, e.g. `round(2.5)` |
| **Help** | Running `help( ... )` will reveal the **help** documentation about a function or type. |
| **Packages** | We can bring external code into our environment with `import ...`. This is how we use **packages**, an essential for Python. Don’t forget to install the package first! |
