# -------------------------------------------------------------------------------
def random() -> _float:
	# Docstring: random
	...


# --------------------------------------------------
@overload
def min(sequence: range_class, /) -> _int: # type: ignore
	# Docstring: min (sequence)
	...

@overload
def min(sequence: Iterable[_float], /) -> _float: # type: ignore
	# Docstring: min (sequence)
	...

@overload
def min(sequence: Iterable[string], /) -> string: # type: ignore
	# Docstring: min (sequence)
	...

@overload
def min(*args: range_class) -> range_class: # type: ignore
	# Docstring: min (literal)
	...

@overload
def min(*args: _float) -> _float: # type: ignore
	# Docstring: min (literal)
	...

@overload
def min(*args: Iterable[_float]) -> Iterable[_float]: # type: ignore
	# Docstring: min (literal)
	...

@overload
def min(*args: string) -> string: # type: ignore
	# Docstring: min (literal)
	...

@overload
def min(*args: Iterable[string]) -> Iterable[string]: # type: ignore
	# Docstring: min (literal)
	...


# --------------------------------------------------
@overload
def max(sequence: range_class, /) -> _int: # type: ignore
	# Docstring: max (sequence)
	...

@overload
def max(sequence: Iterable[_float], /) -> _float: # type: ignore
	# Docstring: max (sequence)
	...

@overload
def max(sequence: Iterable[string], /) -> string: # type: ignore
	# Docstring: max (sequence)
	...

@overload
def max(*args: range_class) -> range_class: # type: ignore
	# Docstring: max (literal)
	...

@overload
def max(*args: _float) -> _float: # type: ignore
	# Docstring: max (literal)
	...

@overload
def max(*args: Iterable[_float]) -> Iterable[_float]: # type: ignore
	# Docstring: max (literal)
	...

@overload
def max(*args: string) -> string: # type: ignore
	# Docstring: max (literal)
	...

@overload
def max(*args: Iterable[string]) -> Iterable[string]: # type: ignore
	# Docstring: max (literal)
	...


# --------------------------------------------------
def abs(x: _float, /) -> _float:
	# Docstring: abs
	...