# -------------------------------------------------------------------------------
type AnyIterable = (
	_dict[_Any, _Any] | _list[_Any] | _set[_Any] | _tuple[_Any] | _str |
	Entities | Grounds | Hats | Items | Leaderboard | Unlocks
)

# --------------------------------------------------
class dict[key: Any, value: Any](_dict):
	# Docstring: dict

	def __init__(self: Self, input: dict[Any, Any] | None = None) -> None:
		...

	def len(self: Self) -> _int:
		# Docstring: len (dict)
		...

	def pop(self: Self, key: Any) -> Any: # type: ignore
		# Docstring: pop (dict)
		...
	...


# --------------------------------------------------
class list[index: Any](_list):
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
class set[key: Any](_set):
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