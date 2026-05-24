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
def add[K: Hashable](given_set: set[K] | _set[K], object: K) -> None:
	# Docstring: add
	...

# --------------------------------------------------
def append[V: Any](given_list: list[V] | _list[V], object: V) -> None:
	# Docstring: append
	...

# --------------------------------------------------
def insert[V: Any](given_list: list[V] | _list[V], index: _float, object: V) -> None:
	# Docstring: insert
	...

# --------------------------------------------------
def len[K: Hashable, V: Any](object : string | dict[K, V] | _dict[K, V] | list[V] | _list[V] | set[K] | _set[K] | tuple[V] | range_class) -> _int:
	# Docstring: len
	...

# --------------------------------------------------
@overload
def pop[K: Hashable, V: Any](collection: dict[K, V] | _dict[K, V], key: K) -> V: # type: ignore
	# Docstring: pop (dict)
	...

@overload
def pop[V: Any](collection: list[V] | _list[V], index: _float) -> V:  # type: ignore
	# Docstring: pop (list)
	...

# --------------------------------------------------
def remove[K: Hashable, V: Any](collection: list[V] | _list[V] | set[K] | _set[K], object: V) -> None:
	# Docstring: remove
	...

# --------------------------------------------------
def str(object: Any) -> string:
	# Docstring: str
	...