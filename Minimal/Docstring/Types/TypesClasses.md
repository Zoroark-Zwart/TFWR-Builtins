# dict

Builds an unordered collection of key-value pairs

dict() -> new empty dictionary

dict(dictionary[keys, values]) -> new dictionary initialized from an existing `dictionary`

takes `1 + len(keys) + len(values)` ticks to execute if a dictionary is given.
takes `1` tick to execute if no input is given.

## len (dict)

Returns the number of items in the dictionary.

returns the length of the dictionary.

takes `1` tick to execute.

example usage:

```
my_dict = {"One": 1, "Two": 2, "Three": 3}
length = len(my_dict)
print(length)
```

Output:

```
3
```

## pop (dict)

Remove the key-value pair corresponding to the `key` in the dict

returns the value of the removed key-value pair

takes `1` tick to execute.

example usage:

```
my_dict = {"One": 1, "Two": 2, "Three": 3}
print("Old Value:", my_dict.pop("One"))
print("Current Dict:", my_dict)
```

Output:

```
Old Value: 1
Current Dict: {"Two":2,"Three":3}
```

# list

Builds an ordered sequence of values.

list() -> new empty list

list(collection: list | tuple | set | str) -> new list from the values of the provided `collection`

list(collection: set | dict) -> new list from the keys of the given `collection`

list(game_enum) -> new list from the values of an in-game enumm `game_enum`

takes `1 + len(collection)` where `collection` is one of the above if an input is given.
takes `1` tick to execute if no input is given.

## append

Add `object` to the end to the list.

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

## insert

Add a `object` to the specified `index` to the list

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

## len (list)

Returns the number of items in the list.

returns the length of the list.

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

## pop (list)

Remove the element corresponding to the `index` in the list. If no index is specified removes the last element in the list.

returns the value of the removed element

takes `len(list) - index` ticks to execute if an `index` is provided
takes `1` tick to execute if no `index` is provided

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

## remove (list)

Remove the element corresponding to the `object` in the list.

takes `# comparions - # shifts` ticks to execute

example usage:

```
my_list = [1, 2, 3]
my_list.remove(1)
print(my_list)
```

Output:

```
[1,3]
```

# set

Builds an unordered collection of elements

set() -> new empty set

set(collection: list | tuple | set | str) -> new set from the values of the provided `collection`

set(collection: set | dict) -> new set from the keys of the given `collection`

set(game_enum) -> new set from the values of an in-game enumm `game_enum`

takes `1 + len(collection)` where `collection` is one of the above if an input is given.
takes `1` tick to execute if no input is given.

## add

Add the `object` to the set.

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

## len (set)

Returns the number of items in the set.

returns the length of the set.

takes `1` tick to execute.

example usage:

```
my_set = {1, 2, 3}
length = len(my_set)
print(length)
```

Output:

```
3
```

## remove (set)

Remove the `object` from the set.

takes `1` tick to execute.

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
