# -------------------------------------------------------------------------------
type Cost = dict[Item, _int] | _dict[Item, _int] | dict[Never, Never]
# Docstring: get_cost (type)

def get_cost(thing: Entity | Entities | Unlock | Unlocks, level: _int = 0, /) -> dict[Item, _int] | _dict[Item, _int] | dict[Never, Never]:
	# Docstring: get_cost
	...


# --------------------------------------------------
def unlock(unlock: Unlock | Unlocks, /) -> _bool:
	# Docstring: unlock
	...


# --------------------------------------------------
def num_unlocked(thing: Enums, /) -> _int:
	# Docstring: num_unlocked
	...