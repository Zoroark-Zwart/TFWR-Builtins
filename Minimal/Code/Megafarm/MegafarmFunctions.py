# -------------------------------------------------------------------------------
def spawn_drone[*P, R: AnyTFWR](task: Callable[[*P], R], /, *args: *P) -> Drone[R] | None:
	# Docstring: spawn_drone
	...


# --------------------------------------------------
def wait_for[R: AnyTFWR](drone: Drone[R], /) -> R:
	# Docstring: wait_for
	...


# --------------------------------------------------
def has_finished[R: AnyTFWR](drone: Drone[R], /) -> _bool:
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