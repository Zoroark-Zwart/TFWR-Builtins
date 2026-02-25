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
def simulate(filename: _str, sim_unlocks: dict[Unlocks, _float] | Iterable[Unlocks] | Unlocks, sim_items: dict[Item, _float], sim_globals: dict[_str, Any], seed: _float, speedup: _float) -> _float:
	# Docstring: simulate
	...