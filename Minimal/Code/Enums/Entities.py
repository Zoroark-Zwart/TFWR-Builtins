# -------------------------------------------------------------------------------
class Entity:
	# Docstring: Entity
	...


# --------------------------------------------------
class Entities(_Enum):
	@staticmethod
	def _generate_next_value_(name: string, start: _int, count: _int, last_values: _list[_Any]) -> Entity:
		return Entity()

	Apple = _auto()
	# Docstring: Apple (Entities)

	Bush = _auto()
	# Docstring: Bush (Entities)

	Cactus = _auto()
	# Docstring: Cactus (Entities)

	Carrot = _auto()
	# Docstring: Carrot (Entities)

	Dead_Pumpkin = _auto()
	# Docstring: Dead_Pumpkin

	Dinosaur = _auto()
	# Docstring: Dinosaur (Entities)

	Grass = _auto()
	# Docstring: Grass (Entities)

	Hedge = _auto()
	# Docstring: Hedge

	Pumpkin = _auto()
	# Docstring: Pumpkin (Entities)

	Sunflower = _auto()
	# Docstring: Sunflower (Entities)

	Treasure = _auto()
	# Docstring: Treasure (Entities)

	Tree = _auto()
	# Docstring: Tree (Entities)