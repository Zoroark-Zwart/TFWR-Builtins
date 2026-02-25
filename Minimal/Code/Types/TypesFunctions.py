# -------------------------------------------------------------------------------
def len(object : _str | dict | list | set | _tuple) -> _int:
	# Docstring: len
	...


# --------------------------------------------------

@overload
def range(stop: _float) -> _range:
	# Docstring: range (stop)
	...

@overload
def range(start: _float, stop: _float) -> _range:
	# Docstring: range (start, stop)
	...

@overload
def range(start: _float, stop: _float, step: _float) -> _range:
	# Docstring: range (start, stop, step)
	...


# --------------------------------------------------
def str(object: Any) -> _str:
	# Docstring: str
	...