# -------------------------------------------------------------------------------
def add(get_set: set[Any], object: Any):
	# Docstring: append
	...

# --------------------------------------------------
def append(given_list: list[Any], object: Any):
	# Docstring: append
	...

# --------------------------------------------------
def insert(given_list: list[Any], object: Any):
	# Docstring: insert
	...

# --------------------------------------------------
def len(object : _str | dict[Any, Any] | list[Any] | set[Any] | _tuple) -> _int:
	# Docstring: len
	...

# --------------------------------------------------
def pop(collection: dict[Any, Any] | list[Any], object: Any):
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
def remove(collection: list[Any] | set[Any], object: Any):
	# Docstring: remove
	...

# --------------------------------------------------
def str(object: Any) -> _str:
	# Docstring: str
	...