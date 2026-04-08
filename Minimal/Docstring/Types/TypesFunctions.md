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

Note: if you wish to type hint a `range` variable use the alias `range_class` instead

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

Note: if you wish to type hint a `range` variable use the alias `range_class` instead

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

Note: if you wish to type hint a `range` variable use the alias `range_class` instead

# remove

Remove the element corresponding to the `object` in a list or set provided as `collection`.

takes `num_comparions + num_shifts` ticks to execute if a list is provided.
takes `1` tick to execute if a set is provided.

example usage:

```
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
```

Output:

```
{1,3}
```

# str

Converts an object to its string representation.

returns the string representation of the object.

takes `1` tick to execute.

example usage:

```
string = str(1000)
print(string)
```

Output:

```
"1000"
```

Note: if you wish to type hint a `str` variable use the alias `string` instead

# MethodFunction

The following definitions are functions that mirror the methods that `lists`, `sets`, and `dicts` have. These definitions can be used as both a method and a function in TFWR.

example usage (method):

```
list_numbers = [1, 2, 3]
last_number = list_numbers.pop()
print(last_number)
```

example usage (function):

```
list_numbers = [1, 2, 3]
last_number = pop(list_numbers)
print(last_number)
```

# add

Add the `object` to a `given_set`.

takes `1` tick to execute.

example usage:

```
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
```

Output:

```
{1,2,3,4}
```

# append

Add `object` to the end of a list provided as `given_list`.

takes `1` tick to execute.

example usage:

```
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
```

Output:

```
[1,2,3,4]
```

# insert

Add a `object` to the specified `index` to a list provided as `given_list`.

takes `1 + len(list) - index` ticks to execute

example usage:

```
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)
```

Output:

```
[1,4,2,3]
```

# len

Returns the number of items in the dict, list, set or str provided as `collection`.

returns the length of the dict, list, set or str.

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

# pop

Remove the element corresponding to the `key` in a dict or list provided as `collection`. If it is a list and no `key` is specified removes the last element in the list.

returns the value of the removed element

takes `len(list) - index` ticks to execute if an index is provided
takes `1` tick to execute if no `key` is provided, of if a dict is provided

example usage:

```
my_list = [1, 2, 3]
print("Old Value:", my_list.pop(1))
print("Current List:", my_list)
```

Output:

```
Old Value: 2
Current List: [1,3]
```
