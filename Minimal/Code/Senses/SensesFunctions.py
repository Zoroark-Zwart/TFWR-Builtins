# -------------------------------------------------------------------------------
def get_entity_type() -> Entity | None:
	# Docstring: get_entity_type
	...


# --------------------------------------------------
def get_ground_type() -> Ground:
	# Docstring: get_ground_type
	...


# --------------------------------------------------
def get_water() -> _float:
	# Docstring: get_water
	...


# --------------------------------------------------
def num_items(item: Item) -> _int | _float:
	# Docstring: num_items
	...


# --------------------------------------------------
def get_companion() -> _tuple[Entity, _tuple[_int, _int]] | None:
	# Docstring: get_companion
	...


# --------------------------------------------------
def measure(direction: Direction | None = None) -> _int | _tuple[_int, _int] | None:
	# Docstring: measure
	...
