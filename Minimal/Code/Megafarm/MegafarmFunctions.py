# -------------------------------------------------------------------------------
def spawn_drone[R: AnyTFWR](task: Callable[..., R]) -> Drone[R]:
	# Docstring: spawn_drone
	...


# --------------------------------------------------
def wait_for[R: AnyTFWR](drone: Drone[R]) -> R:
	# Docstring: wait_for
	...


# --------------------------------------------------
def has_finished(drone: Drone[AnyTFWR]) -> _bool:
	# Docstring: has_finished
	...


# --------------------------------------------------
def max_drones() -> _int:
	# Docstring: max_drones
	...


# --------------------------------------------------
def num_drones() -> _int:
	# Docstring: num_drones
	...