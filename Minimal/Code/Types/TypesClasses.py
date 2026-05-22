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
	tuple[AnyTFWR, ...] |
	_list[AnyTFWR] | _set[AnyTFWR] | _dict[Hashable, AnyTFWR] |		# Python builtins
    list[AnyTFWR] | set[AnyTFWR] | dict[Hashable, AnyTFWR]			# game builtins
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

class dict[K: Hashable, V: AnyTFWR]():
	# Docstring: dict

	def __init__(self: Self, input: dict[K, V] | _dict[K, V] | None = None) -> None:
		...

	def __iter__(self: Self) -> _Iterator[K]:
		...

	def __next__(self: Self) -> K:
		...

	def __getitem__(self: Self, key: K) -> V:
		...

	def __setitem__(self: Self, key: K, object: V) -> None:
		...

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

class list[V: AnyTFWR]():
	# Docstring: list

	def __init__(self: Self, input: AnyIterable | None = None) -> None:
		...

	def __iter__(self: Self) -> _Iterator[V]:
		...

	def __next__(self: Self) -> V:
		...

	def __getitem__(self: Self, index: _float) -> V:
		...

	def __setitem__(self: Self, index: _float, object: V) -> None:
		...

	def __le__(self: Self, compare_list: tuple[V] | list[V] | _list[V]) -> _bool:
		...

	def __lt__(self: Self, compare_list: tuple[V] | list[V] | _list[V]) -> _bool:
		...

	def __ge__(self: Self, compare_list: tuple[V] | list[V] | _list[V]) -> _bool:
		...

	def __gt__(self: Self, compare_list: tuple[V] | list[V] | _list[V]) -> _bool:
		...

	def __iadd__(self: Self, compare_list: list[V] | _list[V]) -> list[V]:
		...

	def __add__(self: Self, compare_list: list[V] | _list[V]) -> list[V]:
		...

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

class set[K: Hashable]():
	# Docstring: set

	def __init__(self: Self, input: AnyIterable | None = None) -> None:
		...

	def __iter__(self: Self) -> _Iterator[K]:
		...

	def __next__(self: Self) -> K:
		...

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

class range_class():
	# Docstring: range_class

	def __iter__(self: Self) -> _Iterator[_int]:
		...

	def __next__(self: Self) -> _int:
		...

	def __getitem__(self: Self, index: _float) -> _int:
		...

	def __le__(self: Self, compare: range_class | list[_int] | _list[_int] | tuple[_int]) -> _bool:
		...

	def __lt__(self: Self, compare: range_class | list[_int] | _list[_int] | tuple[_int]) -> _bool:
		...

	def __ge__(self: Self, compare: range_class | list[_int] | _list[_int] | tuple[_int]) -> _bool:
		...

	def __gt__(self: Self, compare: range_class | list[_int] | _list[_int] | tuple[_int]) -> _bool:
		...

	def len(self: Self) -> _int:
		# Docstring: len (range_class)
		...
	...