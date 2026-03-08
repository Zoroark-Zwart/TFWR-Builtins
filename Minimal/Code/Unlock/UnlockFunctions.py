# -------------------------------------------------------------------------------
def get_cost(thing: Entity | Item | Unlock, level: _int | None = None) -> dict[Item, _int] | None:
	# Docstring: get_cost
	...


# --------------------------------------------------
def unlock(unlock: Unlock) -> _bool:
	# Docstring: unlock
	...


# --------------------------------------------------
def num_unlocked(thing: Unlock | Entity | Ground | Item | Hat) -> _int:
	# Docstring: num_unlocked
	...