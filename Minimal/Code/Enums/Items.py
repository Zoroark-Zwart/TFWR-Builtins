# -------------------------------------------------------------------------------
class Item:
    # Docstring: Item
    ...


# --------------------------------------------------
class Items(_Enum):
    @staticmethod
    def _generate_next_value_(name: string, start: _int, count: _int, last_values: _list[_Any]) -> Item:
        return Item()

    Bone: Item
    # Docstring: Bone (Items)

    Cactus: Item
    # Docstring: Cactus (Items)

    Carrot: Item
    # Docstring: Carrot (Items)

    Fertilizer: Item
    # Docstring: Fertilizer (Items)

    Gold: Item
    # Docstring: Gold (Items)

    Hay: Item
    # Docstring: Hay (Items)

    Piggy: Item
    # Docstring: Piggy (Items)

    Power: Item
    # Docstring: Power (Items)

    Pumpkin: Item
    # Docstring: Pumpkin (Items)

    Water: Item
    # Docstring: Water (Items)

    Weird_Substance: Item
    # Docstring: Weird_Substance (Items)

    Wood: Item
    # Docstring: Wood (Items)