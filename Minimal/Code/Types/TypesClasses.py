# -------------------------------------------------------------------------------
# Docstring: Primitive
type Primitive = _bool | _int | _float | string | None

# --------------------------------------------------
type Enums = (
	Entity | Entities |
    Ground | Grounds | Hat | Hats | Item | Items |
	Leaderboard | Leaderboards | Unlock | Unlocks
)
# Docstring: Enums

# --------------------------------------------------
type Hashable = Primitive | Enums | range_class | Drone | tuple[Hashable, ...]
# Docstring: Hashable

_Hashable_ = TypeVar("_Hashable_", Hashable, Hashable, covariant = True)

# --------------------------------------------------
type Any = (
    Primitive | 								# Python builtin    - basic types

	range_class | Callable[..., Any] |			# Python builtin    - functions / modules

	_tuple[Any,...] | _list[Any] |				# Python builtin    - collection types
    _set[Hashable] | _dict[Hashable, Any] |

	Direction | Enums | 						# Game builtins		- enum classes

	Drone										# Game builtins		- megafarm classes
)
# Docstring: Any

_Any_ = TypeVar("_Any_", Any, Any, covariant = True)

# --------------------------------------------------
type AnyIterable = (
	_dict[Hashable, Any] | _list[Any] | _set[Hashable] | _tuple[Any,...] |
	string | range_class |
	Entities | Grounds | Hats | Items | Leaderboard | Unlocks
)
# Docstring: AnyIterable

# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `dict` methods
# This class requires the use of of the `dict()` constructor. Assigning `dict` literals (ex. `{'1':1, '1':2, '1':3}`) will cause typing conflicts with the builtin Python type `builtins.dict`

# Comment out the `dict` builtins import above to prevent conflict errors.

class dict[key: Hashable, value: Any](_dict):
	# Docstring: dict

	def __init__(self: Self, input: _dict[_Hashable_, _Any_] | None | Container[Hashable] = None) -> None:
		...

	def len(self: Self) -> _int:
		# Docstring: len (dict)
		...

	def pop(self: Self, key: Hashable) -> Any: # type: ignore
		# Docstring: pop (dict)
		...
	...


# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `list` methods
# This class requires the use of of the `list()` constructor. Assigning `list` literals (ex. `[1, 2, 3]`) will cause typing conflicts with the builtin Python type `builtins.list`

# Comment out the `list` builtins import above to prevent conflict errors.

class list[value: Any](_list):
	# Docstring: list

	def __init__(self: Self, input: AnyIterable | None = None) -> None:
		...

	def append(self: Self, object: Any) -> None:
		# Docstring: append
		...

	def insert(self: Self, index: _int, object: Any) -> None: # type: ignore
		# Docstring: insert
		...

	def len(self: Self) -> _int:
		# Docstring: len (list)
		...

	def pop(self: Self, index: _int) -> Any: # type: ignore
		# Docstring: pop (list)
		...

	def remove(self: Self, object: Any) -> None:
		# Docstring: remove (list)
		...
	...


# --------------------------------------------------
# Uncomment this class if you want additional game-specific type hints and docstrings for `set` methods
# This class requires the use of of the `set()` constructor. Assigning set literals (ex. `{1, 2, 3}`) will cause typing conflicts with the builtin Python type `builtins.set`

# Comment out the `set` builtins import above to prevent conflict errors.

class set[value: Hashable](_set):
	# Docstring: set

	def __init__(self: Self, input: AnyIterable | None = None) -> None:
		...

	def add(self: Self, object: Any) -> None:
		# Docstring: add
		...

	def len(self: Self) -> _int:
		# Docstring: len (set)
		...

	def remove(self: Self, object: Any) -> None:
		# Docstring: remove (set)
		...
	...