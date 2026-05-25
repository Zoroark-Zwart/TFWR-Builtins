# -------------------------------------------------------------------------------
def move(direction: Direction, /) -> _bool:
	# Docstring: move
	...


# --------------------------------------------------
def can_move(direction: Direction, /) -> _bool:
	# Docstring: can_move
	...


# --------------------------------------------------
def get_pos_x() -> _int:
	# Docstring: get_pos_x
	...


# --------------------------------------------------
def get_pos_y() -> _int:
	# Docstring: get_pos_y
	...


# --------------------------------------------------
type WorldSizes = Literal[
	3, 4, 5, 6, 7, 8, 9, 10,
	11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
	21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
	31, 32,
]

def get_world_size() -> WorldSizes:
	# Docstring: get_world_size
	...