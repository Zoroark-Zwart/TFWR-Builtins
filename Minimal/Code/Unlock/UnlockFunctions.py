# -------------------------------------------------------------------------------
def get_cost(thing: Entity | Entities | Item | Items | Unlock | Unlocks, level: _int | None = None) -> _dict[Item, _int] | None:
	# Docstring: get_cost
	...


# --------------------------------------------------
def unlock(unlock: Unlock | Unlocks) -> _bool:
	# Docstring: unlock
	...


# --------------------------------------------------
def num_unlocked(thing: Enums) -> _int:
	# Docstring: num_unlocked
	...