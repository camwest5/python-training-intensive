---
title: Programming Building Blocks
--- 

In this workshop we cover the building blocks for developing more complex code, looking at

* Understanding variable types and methods
* Conditionals
* Loops
* Custom functions

## Directing traffic with conditionals
In the first half of this session we'll look at two types of control flows: **conditionals** and **loops**.

Conditionals allow you to put "gates" in your code, only running sections if a certain **condition** is true. They are common to most programming languages.

In Python, they are called `if` statements, because you use the `if` command. For example,

```python
if 5 > 0:
    print("We're inside the if statement")
```

The line `print("We're inside the if statement")` **will only run if `5 > 0` is true**. If not, it'll get skipped.

Indents are essential. Only indented code will be governed by conditional

```python
if 5 > 0:
    print("We're inside the if statement")

print("This code always runs")
```

Watch what happens if we change the condition

```python
if 5 > 10:
    print("We're inside the if statement")

print("This code always runs")
```

Now, the first line **doesn't run**. That's the essence of a conditional.

There's not much point to using a condition that will always be true. Typically, you'd use a variable in the condition, for example.

```python
pet_age = 10

if pet_age > 10:
    print("My pet is older than 10")
```

### Logical operators

Here is a table of the different operators you can make conditions with. When you run them, they always return either `True` or `False`. 

| Operator | True example | Description |
| --- | --- | --- |
| `==` | `10 == 10` | Same value and type |
| `!=` | `"10" != 10` | Different value **or** type |
| `>` | `10 > 5` | Greater than |
| `>=` | `10 >= 10` | Greater than or equal to |
| `<` | `5 < 10` | Less than |
| `<=` | `5 <= 10` | Less than or equal to |
| `in` | `"a" in "apple"` | First object exists in the second
| `not in` | `"b" not in "apple"` | First object **does not** exist in the second |
| `and` | `10 == 10 and "a" in "apple"` | Only true if **both** conditions are true. Same as `&` |
| `or` | `10 == 10 or "b" in "apple"` | Always true if **one** condition is true. Same as `\|` |

### `elif` and `else`

`if` statements only run if the condition is **True**. What happens if its **False**? That's what the `else` command is for, it's like a net that catches anything that slipped past `if`:

```python
pet_age = 5

if pet_age > 10:
    print("My pet is older than 10")
else:
    print("My pet is 10 or younger")
```

> Don't forget the colon `:`!

Check what happens when you change the age from 5 to 15.

Finally, what if you wanted to check another condition **only if the first one fails**? That's what `elif` (else-if) is for. It's another if statement but it only runs if the first fails.

```python
pet_age = 5

if pet_age > 10:
    print("My pet is older than 10")
elif pet_age < 5:
    print("My pet is younger than 5")
else:
    print("My pet is between 5 and 10")
```

You can include as many as you'd like
```python
pet_age = 5

if pet_age > 10:
    print("My pet is older than 10")
elif pet_age < 5:
    print("My pet is younger than 5")
elif pet_age < 1:
    print("My pet is freshly born")
else:
    print("My pet is between 5 and 10")
```

## Repeat after me

## Looking under the hood: what makes `ints` *ints*?

Why *do* we have all these different variable types? Wouldn't it be simpler to just have two or three, like float string and list?



## Building your own machines