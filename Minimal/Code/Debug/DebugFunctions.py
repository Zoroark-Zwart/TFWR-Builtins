# -------------------------------------------------------------------------------
def get_time() -> _float:
	# Docstring: get_time
	...


# --------------------------------------------------
def get_tick_count() -> _int:
	# Docstring: get_tick_count
	...


# --------------------------------------------------
def set_execution_speed(speed: _float) -> None:
	# Docstring: set_execution_speed
	...


# --------------------------------------------------
def set_world_size(size: _float) -> None:
	# Docstring: set_world_size
	...


# --------------------------------------------------
type SimulateUnlocks = _dict[Unlock, _int] | _tuple[_tuple[Unlock, _int]] | _list[_tuple[Unlock, _int]] | _tuple[Unlock] | _list[Unlock] | Unlocks

def simulate(
		filename: string,
		sim_unlocks: SimulateUnlocks,
		sim_items: _dict[Item, _float],
		sim_globals: _dict[string, Any],
		seed: _float, speedup: _float
	) -> _float:
	# Docstring: simulate
	...