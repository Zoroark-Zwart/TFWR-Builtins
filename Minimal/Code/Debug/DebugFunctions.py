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
type WorldSizes = Literal[
	3, 4, 5, 6, 7, 8, 9, 10,
	11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
	21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
	31, 32,
]

def set_world_size(size: WorldSizes, /) -> None:
	# Docstring: set_world_size
	...


# --------------------------------------------------
type SimulateUnlocks = _dict[Unlock, _int] | _tuple[_tuple[Unlock, _int]] | _list[_tuple[Unlock, _int]] | _tuple[Unlock] | _list[Unlock] | Unlocks

def simulate(
		filename: string,
		sim_unlocks: SimulateUnlocks,
		sim_items: _dict[Item, _float],
		sim_globals: _dict[string, AnyTFWR],
		seed: _float, speedup: _float,
		/
	) -> _float:
	# Docstring: simulate
	...