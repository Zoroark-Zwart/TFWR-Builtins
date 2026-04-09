# -------------------------------------------------------------------------------
class Entity:
	# Docstring: Entity
	...


# --------------------------------------------------
class Entities(_Enum):
	@staticmethod
	def _generate_next_value_(name: string, start: _int, count: _int, last_values: _list[_Any]) -> Entity:
		return Entity()

	Apple: Entity
	# Docstring: Apple (Entities)

	Bush: Entity
	# Docstring: Bush (Entities)

	Cactus: Entity
	# Docstring: Cactus (Entities)

	Carrot: Entity
	# Docstring: Carrot (Entities)

	Dead_Pumpkin: Entity
	# Docstring: Dead_Pumpkin

	Dinosaur: Entity
	# Docstring: Dinosaur (Entities)

	Grass: Entity
	# Docstring: Grass (Entities)

	Hedge: Entity
	# Docstring: Hedge

	Pumpkin: Entity
	# Docstring: Pumpkin (Entities)

	Sunflower: Entity
	# Docstring: Sunflower (Entities)

	Treasure: Entity
	# Docstring: Treasure (Entities)

	Tree: Entity
	# Docstring: Tree (Entities)