# -------------------------------------------------------------------------------
class Ground:
	# Docstring: Ground
	...


# --------------------------------------------------
class Grounds(_Enum):
	@staticmethod
	def _generate_next_value_(name: string, start: _int, count: _int, last_values: _list[_Any]) -> Ground:
		return Ground()

	Grassland: Ground
	# Docstring: Grassland

	Soil: Ground
	# Docstring: Soil