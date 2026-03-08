# -------------------------------------------------------------------------------
def add(get_set: _set[Any], object: Any):
	# Docstring: append
	...

# --------------------------------------------------
def append(given_list: _list[Any], object: Any):
	# Docstring: append
	...

# --------------------------------------------------
def insert(given_list: _list[Any], object: Any):
	# Docstring: insert
	...

# --------------------------------------------------
def len(object : _str | _dict[Any, Any] | _list[Any] | _set[Any] | _tuple[Any]) -> _int:
	# Docstring: len
	...

# --------------------------------------------------
def pop(collection: _dict[Any, Any] | _list[Any], object: Any):
	# Docstring: pop
	...

# --------------------------------------------------
@overload
def range(stop: _float) -> _range:  # type: ignore
	# Docstring: range (stop)
	...

@overload
def range(start: _float, stop: _float) -> _range:  # type: ignore
	# Docstring: range (start, stop)
	...

@overload
def range(start: _float, stop: _float, step: _float) -> _range:  # type: ignore
	# Docstring: range (start, stop, step)
	...

# --------------------------------------------------
def remove(collection: _list[Any] | _set[Any], object: Any):
	# Docstring: remove
	...

# --------------------------------------------------
def str(object: Any) -> _str:
	# Docstring: str
	...