# -------------------------------------------------------------------------------
def add(get_set: set, object: Any):
	# Docstring: append
	...

# --------------------------------------------------
def append(given_list: list, object: Any):
	# Docstring: append
	...

# --------------------------------------------------
def insert(given_list: list, object: Any):
	# Docstring: insert
	...

# --------------------------------------------------
def len(object : _str | dict | list | set | _tuple) -> _int:
	# Docstring: len
	...

# --------------------------------------------------
def pop(collection: dict | list, object: Any):
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
def remove(collection: list | set, object: Any):
	# Docstring: remove
	...

# --------------------------------------------------
def str(object: Any) -> _str:
	# Docstring: str
	...