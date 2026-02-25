# len

Returns the number of items in an object.

returns the length of the object.

takes `1` tick to execute.

example usage:

```
my_list = [1, 2, 3]
length = len(my_list)
print(length)
```

Output:

```
3
```

# range (stop)

Returns a sequence of numbers from `0` (inclusive) to `stop` (exclusive).

returns a range object.

takes `1` tick to execute.

example usage:

```
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

# range (start, stop)

Returns a sequence of numbers from `start` (inclusive) to `stop` (exclusive).

returns a range object.

takes `1` tick to execute.

example usage:

```
for i in range(2, 5):
    print(i)
```

Output:

```
2
3
4
```

# range (start, stop, step)

Returns a sequence of numbers from `start` (inclusive) to `stop` (exclusive) every `step` interval.

returns a range object.

takes `1` tick to execute.

example usage:

```
for i in range(2, 5, 2):
    print(i)
```

Output:

```
2
4
```

# str

Converts an object to its string representation.

returns the string representation of the object.

takes `1` tick to execute.

example usage:

```
string = _str(1000)
print(string)
```

Output:

```
"1000"
```
