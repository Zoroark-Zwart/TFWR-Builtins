# random

Samples a random number between 0 (inclusive) and 1 (exclusive).

returns the random number.

takes `1` ticks to execute.

example usage:

```
def random_elem(list):
    index = random() * len(list) // 1
    return list[index]
```

# min (sequence)

Gets the minimum of a sequence of elements. Elements can be `float` or `str`

`sequence`: Any `tuple`, `list`, `dict` or `set`

`min(sequence)`: Returns the minimum of all values in a sequence.

returns the minimum value from the arguments.

takes `num_comparison` ticks to execute.

example usage:

```
smallest_from_list = min([3, 6, 34, 16])
```

# min (literal)

Gets the minimum of several passed arguments. Can be used on `float` or `str`

`min(a,b,c)`: Returns the minimum of `a`, `b` and `c`.

returns the minimum value from the arguments.

takes `num_comparison` ticks to execute.

example usage:

```
smallest = min(1, 5, 3, 2)
```

# max (sequence)

Gets the maximum of a sequence of elements. Elements can be `float` or `str`

`sequence`: Any `tuple`, `list`, `dict` or `set`

`max(sequence)`: Returns the maximum of all values in a sequence.

returns the maximum value from the arguments.

takes `num_comparison` ticks to execute.

example usage:

```
smallest_from_list = max([3, 6, 34, 16])
```

# max (literal)

Gets the maximum of several passed arguments. Can be used on `float` or `str`.

`max(a,b,c)`: Returns the maximum of `a`, `b` and `c`.

returns the maximum value from the arguments.

takes `num_comparison` ticks to execute.

example usage:

```
smallest = max(1, 5, 3, 2)
```

# abs

Returns the absolute value of a number.

returns the absolute value of x.

takes `1` tick to execute.

example usage:

```
positive = abs(-5)
print(positive)
```

Output:

```
5
```
