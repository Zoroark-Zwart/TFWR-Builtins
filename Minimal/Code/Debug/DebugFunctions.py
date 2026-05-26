# -------------------------------------------------------------------------------
def get_time() -> _float:
	# Docstring: get_time
	...


# --------------------------------------------------
def get_tick_count() -> _int:
	# Docstring: get_tick_count
	...


# --------------------------------------------------
def set_execution_speed(speed: _float, /) -> None:
	# Docstring: set_execution_speed
	...


# --------------------------------------------------
def set_world_size(size: WorldSizes, /) -> None:
	# Docstring: set_world_size
	...


# --------------------------------------------------
type _SimulateUnlocksPair = _tuple[Unlock, _int]

type SimulateUnlocks = (
	dict[Unlock, _int] | _dict[Unlock, _int] |					# (Unlock, int) pairings
	list[_SimulateUnlocksPair] | _list[_SimulateUnlocksPair] |
	_tuple[_SimulateUnlocksPair,...] |

	_tuple[Unlock,...] |										# Sequence of unlocks
	_list[Unlock] |

	Unlocks														# All unlocks
)
# Docstring: simulate (unlocks)

type SimulateItems = dict[Item, _float] | _dict[Item, _float]
# Docstring: simulate (items)

type SimulateGlobals = dict[string, AnyTFWR] | _dict[string, AnyTFWR]
# Docstring: simulate (globals)

def simulate(
		filename: string,
		sim_unlocks: SimulateUnlocks,
		sim_items: dict[Item, _float] | _dict[Item, _float],
		sim_globals: dict[string, AnyTFWR] | _dict[string, AnyTFWR],
		seed: _float, speedup: _float,
		/
	) -> _float:
	# Docstring: simulate
	...