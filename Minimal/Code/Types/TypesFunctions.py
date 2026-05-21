# -------------------------------------------------------------------------------
@overload
def range(stop: _float) -> range_class:  # type: ignore
	# Docstring: range (stop)
	...

@overload
def range(start: _float, stop: _float) -> range_class:  # type: ignore
	# Docstring: range (start, stop)
	...

@overload
def range(start: _float, stop: _float, step: _float) -> range_class:  # type: ignore
	# Docstring: range (start, stop, step)
	...

# --------------------------------------------------
# Docstring: MethodFunction

# --------------------------------------------------
def add(given_set: _set[_Hashable_], object: Any) -> None:
	# Docstring: add
	...

# --------------------------------------------------
def append(given_list: _list[_Any_], object: Any) -> None:
	# Docstring: append
	...

# --------------------------------------------------
def insert(given_list: _list[_Any_], index: _int, object: Any) -> None:
	# Docstring: insert
	...

# --------------------------------------------------
def len(object : string | _dict[_Hashable_, _Any_] | _list[_Any_] | _set[_Hashable_] | _tuple[_Any_] | range_class) -> _int:
	# Docstring: len
	...

# --------------------------------------------------
def pop(collection: _dict[_Hashable_, _Any_] | _list[_Any_], object: Any):
	# Docstring: pop
	...

# --------------------------------------------------
def remove(collection: _list[_Any_] | _set[_Hashable_], object: Any):
	# Docstring: remove
	...

# --------------------------------------------------
def str(object: Any) -> string:
	# Docstring: str
	...