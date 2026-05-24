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

Gets the minimum of a sequence of elements. Elements can be `float` or `str` unless a `range` is given then elements will be `int`.

`sequence`: Any `tuple`, `list`, `range`, `dict`, or `set`

`min(sequence)`: Returns the minimum of all values in a sequence.

returns the minimum from the arguments:
- If `tuple`, `list` or `range` is given will return minimum value
- If `dict` or `set` is given will return the minimum key.

takes `num_comparison` ticks to execute.

example usage:

```
smallest_from_list = min([3, 6, 34, 16])
```

# min (literal)

Gets the minimum of several passed arguments. Can be used on `float` or `str` unless a `range` is given then elements will be `int`.

`min(a,b,c)`: Returns the minimum of `a`, `b` and `c`.

returns the collection that has the minimum total:
- If `tuple`, `list` or `range` is given will return minimum argument based onvalue
- If `dict` or `set` is given will return the minimum argument based on key.

takes `num_comparison` ticks to execute.

example usage:

```
smallest = min(1, 5, 3, 2)
```

# max (sequence)

Gets the maximum of a sequence of elements. Elements can be `float` or `str` unless a `range` is given then elements will be `int`.

`sequence`: Any `tuple`, `list`, `range`, `dict`, or `set`

`max(sequence)`: Returns the maximum of all values in a sequence.

returns the maximum from the arguments:
- If `tuple`, `list` or `range` is given will return maximum value
- If `dict` or `set` is given will return the maximum key.

takes `num_comparison` ticks to execute.

example usage:

```
smallest_from_list = max([3, 6, 34, 16])
```

# max (literal)

Gets the maximum of several passed arguments. Can be used on `float` or `str` unless a `range` is given then elements will be `int`.

`max(a,b,c)`: Returns the maximum of `a`, `b` and `c`.

returns the collection that has the maximum total:
- If `tuple`, `list` or `range` is given will return maximum argument based onvalue
- If `dict` or `set` is given will return the maximum argument based on key.

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
