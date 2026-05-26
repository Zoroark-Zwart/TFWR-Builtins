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
	dict[Hashable, AnyTFWR] | _dict[Hashable, AnyTFWR] |
	set[Hashable] | _set[Hashable] |
	list[AnyTFWR] | _list[AnyTFWR] |
	_tuple[AnyTFWR,...]
)

type AnyTFWR = (
    Primitive |	range_class | _range |		# Python builtin    - basic types

	Callable[..., AnyTFWR] | ModuleType |	# Python builtin    - functions / modules

	_AnyCollection |						# Both builtins     - collection types

	Direction | Enums | 					# Game builtins		- enum classes

	Drone[AnyTFWR]							# Game builtins		- megafarm classes
)
# Docstring: AnyTFWR

# --------------------------------------------------
type AnyIterable = (
	string | range_class | _range | _AnyCollection |
	Entities | Grounds | Hats | Items | Leaderboards | Unlocks
)
# Docstring: AnyIterable

# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `dict` methods
# This class requires the use of of the `dict()` constructor. Assigning `dict` literals (ex. `{'1':1, '1':2, '1':3}`) will cause typing conflicts with the builtin Python type `builtins.dict`

# Comment out the `dict` builtins import above to prevent conflict errors.

type DictTFWR[K: Any, V: Any] = dict[K, V] | _dict[K, V]
# Docstring: dict (type)
class dict[K: Hashable, V: Any]():
	# Docstring: dict
	def __init__(self: Self, input: DictTFWR[K, V] | None = None, /) -> None: ...
	def __iter__(self: Self, /) -> Iterator[K]: ...
	def __next__(self: Self, /) -> K: ...
	def __getitem__(self: Self, key: K, /) -> V: ...
	def __setitem__(self: Self, key: K, object: V, /) -> None: ...
	def __contains__(self, compare_object: K, /) -> _bool: ...
	def len(self: Self, /) -> _int:
		# Docstring: len (dict)
		...
	def pop(self: Self, key: K, /) -> V:
		# Docstring: pop (dict)
		...
	...

# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `list` methods
# This class requires the use of of the `list()` constructor. Assigning `list` literals (ex. `[1, 2, 3]`) will cause typing conflicts with the builtin Python type `builtins.list`

# Comment out the `list` builtins import above to prevent conflict errors.

type ListTFWR[V: AnyTFWR] = list[V] | _list[V]
# Docstring: list (type)
class list[V: Any]():
	# Docstring: list
	def __init__(self: Self, input: Iterable[V] | None = None, /) -> None: ...
	def __iter__(self: Self, /) -> Iterator[V]: ...
	def __next__(self: Self, /) -> V: ...
	def __getitem__(self: Self, index: _float, /) -> V: ...
	def __setitem__(self: Self, index: _float, object: V, /) -> None: ...
	def __le__(self: Self, compare_list: tuple[V,...] | ListTFWR[V], /) -> _bool: ...
	def __lt__(self: Self, compare_list: tuple[V,...] | ListTFWR[V], /) -> _bool: ...
	def __ge__(self: Self, compare_list: tuple[V,...] | ListTFWR[V], /) -> _bool: ...
	def __gt__(self: Self, compare_list: tuple[V,...] | ListTFWR[V], /) -> _bool: ...
	def __iadd__(self: Self, compare_list: ListTFWR[V], /) -> list[V]: ...
	def __add__(self: Self, compare_list: ListTFWR[V], /) -> list[V]: ...
	def __contains__(self, compare_object: V, /) -> _bool: ...
	def append(self: Self, object: V, /) -> None:
		# Docstring: append
		...
	def insert(self: Self, index: _float, object: V, /) -> None: # type: ignore
		# Docstring: insert
		...
	def len(self: Self, /) -> _int:
		# Docstring: len (list)
		...
	def pop(self: Self, index: _float = -1, /) -> V: # type: ignore
		# Docstring: pop (list)
		...
	def remove(self: Self, object: V, /) -> None:
		# Docstring: remove (list)
		...
	...


# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `set` methods
# This class requires the use of of the `set()` constructor. Assigning set literals (ex. `{1, 2, 3}`) will cause typing conflicts with the builtin Python type `builtins.set`

# Comment out the `set` builtins import above to prevent conflict errors.

type SetTFWR[K: Hashable] = set[K] | _set[K]
# Docstring: set (type)
class set[K: Hashable]():
	# Docstring: set
	def __init__(self: Self, input: Iterable[K] | None = None, /) -> None: ...
	def __iter__(self: Self, /) -> Iterator[K]: ...
	def __next__(self: Self, /) -> K: ...
	def __contains__(self, compare_object: K, /) -> _bool: ...
	def add(self: Self, object: K, /) -> None:
		# Docstring: add
		...
	def len(self: Self, /) -> _int:
		# Docstring: len (set)
		...
	def remove(self: Self, object: K, /) -> None:
		# Docstring: remove (set)
		...
	...

# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `range_class` methods. Should use in conjunction with the `range` function.

# Comment out the `range_class` builtins import above to prevent conflict errors.

type RangeTFWR = range_class | _range
# Docstring: range (type)
class range_class():
	# Docstring: range_class
	def __iter__(self: Self, /) -> Iterator[_int]: ...
	def __next__(self: Self, /) -> _int: ...
	def __getitem__(self: Self, index: _float, /) -> _int: ...
	def __le__(self: Self, compare: range_class | list[_int] | _list[_int] | tuple[_int], /) -> _bool:
		# Docstring: compare (range_class)
		...
	def __lt__(self: Self, compare: range_class | list[_int] | _list[_int] | tuple[_int], /) -> _bool:
		# Docstring: compare (range_class)
		...
	def __ge__(self: Self, compare: range_class | list[_int] | _list[_int] | tuple[_int], /) -> _bool:
		# Docstring: compare (range_class)
		...
	def __gt__(self: Self, compare: range_class | list[_int] | _list[_int] | tuple[_int], /) -> _bool:
		# Docstring: compare (range_class)
		...
	def __contains__(self, compare_value: _int, /) -> _bool: ...
	def len(self: Self, /) -> _int:
		# Docstring: len (range_class)
		...
	...