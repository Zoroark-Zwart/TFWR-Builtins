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
def add[K: Hashable](given_set: set[K], object: K) -> None:
	# Docstring: add
	...

# --------------------------------------------------
def append[V: AnyTFWR](given_list: list[V], object: V) -> None:
	# Docstring: append
	...

# --------------------------------------------------
def insert[V: AnyTFWR](given_list: list[V], index: _float, object: V) -> None:
	# Docstring: insert
	...

# --------------------------------------------------
def len[_K: Hashable, V: AnyTFWR](object : string | dict[_K, V] | list[V] | set[_K] | tuple[V] | range_class) -> _int:
	# Docstring: len
	...

# --------------------------------------------------
@overload
def pop[_K: Hashable, V: AnyTFWR](collection: dict[_K, V], key: _K) -> V: # type: ignore
	# Docstring: pop (dict)
	...

@overload
def pop[V: AnyTFWR](collection: list[V], index: _float) -> V:  # type: ignore
	# Docstring: pop (list)
	...

# --------------------------------------------------
def remove[_K: Hashable, V: AnyTFWR](collection: list[V] | set[_K], object: V) -> None:
	# Docstring: remove
	...

# --------------------------------------------------
def str(object: Any) -> string:
	# Docstring: str
	...