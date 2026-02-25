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

# min

Gets the minimum of a sequence of elements or several passed arguments.
Can be used on numbers and strings.

`min(a,b,c)`: Returns the minimum of `a`, `b` and `c`.
`min(sequence)`: Returns the minimum of all values in a sequence.

returns the minimum value from the arguments.

takes #comparisons ticks to execute.

example usage:

```
smallest = min(1, 5, 3, 2)
smallest_from_list = min([3, 6, 34, 16])
```

# max

Gets the maximum of a sequence of elements or several passed arguments.
Can be used on numbers and strings.

`max(a,b,c)`: Returns the maximum of `a`, `b` and `c`.
`max(sequence)`: Returns the maximum of all values in a sequence.

returns the maximum value from the arguments.

takes #comparisons ticks to execute.

example usage:

```
largest = max(1, 5, 3, 2)
largest_from_list = max([3, 6, 34, 16])
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
