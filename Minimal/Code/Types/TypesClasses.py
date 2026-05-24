# -------------------------------------------------------------------------------
type Primitive = _bool | _int | _float | string | None
# Docstring: Primitive

# --------------------------------------------------
type Enums = (
	Entity | Entities |
    Ground | Grounds | Hat | Hats | Item | Items |
	Leaderboard | Leaderboards | Unlock | Unlocks
)
# Docstring: Enums

# --------------------------------------------------
type Hashable = (
    Primitive | range_class |
	tuple[Hashable, ...] |
	Enums |
	Drone[AnyTFWR]
)
# Docstring: Hashable

# --------------------------------------------------
type _AnyCollection = (
	_tuple[AnyTFWR,...] |

	dict[_int, AnyTFWR] | _dict[_int, AnyTFWR] |
	dict[_float, AnyTFWR] | _dict[_float, AnyTFWR] |
	dict[string, AnyTFWR] | _dict[string, AnyTFWR] |
	dict[None, AnyTFWR] | _dict[None, AnyTFWR] |

	set[_int] | _set[_int] |
	set[_float] | _set[_float] |
	set[string] | _set[string] |
	set[None] | _set[None] |

	list[_int] | _list[_int] |
	list[_float] | _list[_float] |
	list[string] | _list[string] |
	list[None] | _list[None] |

	list[Entity] | _list[Entity] |
	list[Entities] | _list[Entities] |
	list[Ground] | _list[Ground] |
	list[Grounds] | _list[Grounds] |
	list[Hat] | _list[Hat] |
	list[Hats] | _list[Hats] |
	list[Item] | _list[Item] |
	list[Items] | _list[Items] |
	list[Leaderboard] | _list[Leaderboard] |
	list[Leaderboards] | _list[Leaderboards] |
	list[Unlock] | _list[Unlock] |
	list[Unlocks] | _list[Unlocks] |


	dict[Entity, AnyTFWR] | _dict[Entity, AnyTFWR] |
	dict[Entities, AnyTFWR] | _dict[Entities, AnyTFWR] |
	dict[Ground, AnyTFWR] | _dict[Ground, AnyTFWR] |
	dict[Grounds, AnyTFWR] | _dict[Grounds, AnyTFWR] |
	dict[Hat, AnyTFWR] | _dict[Hat, AnyTFWR] |
	dict[Hats, AnyTFWR] | _dict[Hats, AnyTFWR] |
	dict[Item, AnyTFWR] | _dict[Item, AnyTFWR] |
	dict[Items, AnyTFWR] | _dict[Items, AnyTFWR] |
	dict[Leaderboard, AnyTFWR] | _dict[Leaderboard, AnyTFWR] |
	dict[Leaderboards, AnyTFWR] | _dict[Leaderboards, AnyTFWR] |
	dict[Unlock, AnyTFWR] | _dict[Unlock, AnyTFWR] |
	dict[Unlocks, AnyTFWR] | _dict[Unlocks, AnyTFWR] |

	set[Entity] | _set[Entity] |
	set[Entities] | _set[Entities] |
	set[Ground] | _set[Ground] |
	set[Grounds] | _set[Grounds] |
	set[Hat] | _set[Hat] |
	set[Hats] | _set[Hats] |
	set[Item] | _set[Item] |
	set[Items] | _set[Items] |
	set[Leaderboard] | _set[Leaderboard] |
	set[Leaderboards] | _set[Leaderboards] |
	set[Unlock] | _set[Unlock] |
	set[Unlocks] | _set[Unlocks]
)

type AnyTFWR = (
    Primitive |	range_class |				# Python builtin    - basic types

	Callable[..., AnyTFWR] | ModuleType |	# Python builtin    - functions / modules

	_AnyCollection |						# Both builtins     - collection types

	Direction | Enums | 					# Game builtins		- enum classes

	Drone[AnyTFWR]							# Game builtins		- megafarm classes
)
# Docstring: AnyTFWR

# --------------------------------------------------
type AnyIterable = (
	string | range_class | _AnyCollection |
	Entities | Grounds | Hats | Items | Leaderboards | Unlocks
)
# Docstring: AnyIterable

# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `dict` methods
# This class requires the use of of the `dict()` constructor. Assigning `dict` literals (ex. `{'1':1, '1':2, '1':3}`) will cause typing conflicts with the builtin Python type `builtins.dict`

# Comment out the `dict` builtins import above to prevent conflict errors.

type DictType[k: Hashable, v: Any] = dict[k, v] | _dict[k, v]
"""
This type is used to represent the custom dict type that is specific to the game and the dict type provided by Python's builtins module. It is used to help you manage custom dicts and dict literals such as `{1: "One", 2: "Two", 3: "Three"]`. You cannot assign a dict literal to the custom dict type, however.
"""

class dict[K: Hashable, V: Any]():
	# Docstring: dict

	def __init__(self: Self, input: DictType[K, V] | None = None) -> None: ...

	def __iter__(self: Self) -> _Iterator[K]: ...

	def __next__(self: Self) -> K: ...

	def __getitem__(self: Self, key: K) -> V: ...

	def __setitem__(self: Self, key: K, object: V) -> None: ...

	def __contains__(self, compare_object: K) -> _bool: ...

	def len(self: Self) -> _int:
		# Docstring: len (dict)
		...

	def pop(self: Self, key: K) -> V:
		# Docstring: pop (dict)
		...
	...


# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `list` methods
# This class requires the use of of the `list()` constructor. Assigning `list` literals (ex. `[1, 2, 3]`) will cause typing conflicts with the builtin Python type `builtins.list`

# Comment out the `list` builtins import above to prevent conflict errors.

type ListType[V: Any] = list[V] | _list[V]
"""
This type is used to represent the custom list type that is specific to the game and the list type provided by Python's builtins module. It is used to help you manage custom lists and list literals such as `[1, 2, 3]`. You cannot assign a list literal to the custom list type, however.
"""

class list[V: Any]():
	# Docstring: list

	def __init__(self: Self, input: Iterable[V] | None = None) -> None: ...

	def __iter__(self: Self) -> _Iterator[V]: ...

	def __next__(self: Self) -> V: ...

	def __getitem__(self: Self, index: _float) -> V: ...

	def __setitem__(self: Self, index: _float, object: V) -> None: ...

	def __le__(self: Self, compare_list: tuple[V] | ListType[V]) -> _bool: ...

	def __lt__(self: Self, compare_list: tuple[V] | ListType[V]) -> _bool: ...

	def __ge__(self: Self, compare_list: tuple[V] | ListType[V]) -> _bool: ...

	def __gt__(self: Self, compare_list: tuple[V] | ListType[V]) -> _bool: ...

	def __iadd__(self: Self, compare_list: ListType[V]) -> list[V]: ...

	def __add__(self: Self, compare_list: ListType[V]) -> list[V]: ...

	def __contains__(self, compare_object: V) -> _bool: ...

	def append(self: Self, object: V) -> None:
		# Docstring: append
		...

	def insert(self: Self, index: _float, object: V) -> None: # type: ignore
		# Docstring: insert
		...

	def len(self: Self) -> _int:
		# Docstring: len (list)
		...

	def pop(self: Self, index: _float) -> V: # type: ignore
		# Docstring: pop (list)
		...

	def remove(self: Self, object: V) -> None:
		# Docstring: remove (list)
		...
	...


# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `set` methods
# This class requires the use of of the `set()` constructor. Assigning set literals (ex. `{1, 2, 3}`) will cause typing conflicts with the builtin Python type `builtins.set`

# Comment out the `set` builtins import above to prevent conflict errors.

type SetType[K: Hashable] = set[k] | _set[K]
"""
This type is used to represent the custom set type that is specific to the game and the set type provided by Python's builtins module. It is used to help you manage custom lists and set literals such as `{1, 2, 3}`. You cannot assign a set literal to the custom set type, however.
"""

class set[K: Hashable]():
	# Docstring: set

	def __init__(self: Self, input: Iterable[K] | None = None) -> None: ...

	def __iter__(self: Self) -> _Iterator[K]: ...

	def __next__(self: Self) -> K: ...

	def __contains__(self, compare_object: K) -> _bool: ...

	def add(self: Self, object: K) -> None:
		# Docstring: add
		...

	def len(self: Self) -> _int:
		# Docstring: len (set)
		...

	def remove(self: Self, object: K) -> None:
		# Docstring: remove (set)
		...
	...

# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `range_class` methods. Should use in conjunction with the `range` function.

# Comment out the `range_class` builtins import above to prevent conflict errors.

type RangeType = range_class | _range
"""
This type is used to represent the custom range type that is specific to the game and the range type provided by Python's builtins module. You cannot assign a range literal to the custom range type, however.
"""

class range_class():
	# Docstring: range_class

	def __iter__(self: Self) -> _Iterator[_int]: ...

	def __next__(self: Self) -> _int: ...

	def __getitem__(self: Self, index: _float) -> _int: ...

	def __le__(self: Self, compare: range_class | list[_int] | _list[_int] | tuple[_int]) -> _bool:
		# Docstring: compare (range_class)
		...

	def __lt__(self: Self, compare: range_class | list[_int] | _list[_int] | tuple[_int]) -> _bool:
		# Docstring: compare (range_class)
		...

	def __ge__(self: Self, compare: range_class | list[_int] | _list[_int] | tuple[_int]) -> _bool:
		# Docstring: compare (range_class)
		...

	def __gt__(self: Self, compare: range_class | list[_int] | _list[_int] | tuple[_int]) -> _bool:
		# Docstring: compare (range_class)
		...

	def __contains__(self, compare_value: _int) -> _bool: ...

	def len(self: Self) -> _int:
		# Docstring: len (range_class)
		...
	...