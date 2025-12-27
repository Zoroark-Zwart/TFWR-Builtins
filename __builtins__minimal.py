# This file gives Python type definitions to TFWR builtins to allow editing code with Python editors.
# Note that the games language is not Python and these definitions are only an approximation.

# Contributed by @Noon, @KlingonDragon, @dieckie, @Flekay and @Zoroark-Zwart on the TFWR Discord server.

from typing import Any
from collections.abc import Iterable
from builtins import (bool as _bool, int as _int, float as _float, str as _str,
					  range as _range,
					  tuple as _tuple, list as _list, set as _set, dict as _dict)

# Section: Imports



# -------------------------------------------------------------------------------
# In-Game Enums
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
class Item:
    """
    A member of the Items Class
    """
    ...


class Items:
    Bone: Item
    """
    The bones of an ancient creature.
    """

    Cactus: Item
    """
    Obtained by harvesting sorted cacti.
    """

    Carrot: Item
    """
    Obtained by harvesting carrots.
    """

    Fertilizer: Item
    """
    Call `use_item(Items.Fertilizer)` to instantly remove 2s from the plants remaining grow time.
    """

    Gold: Item
    """
    Found in treasure chests in mazes.
    """

    Hay: Item
    """
    Obtained by cutting grass.
    """

    Piggy: Item
    """
    This item has been removed from the game but remains as a nostalgia trophy.
    """

    Power: Item
    """
    Obtained by harvesting sunflowers. The drone automatically uses this to move twice as fast.
    """

    Pumpkin: Item
    """
    Obtained by harvesting pumpkins.
    """

    Water: Item
    """
    Used to water the ground by calling `use_item(Items.Water)`.
    """

    Weird_Substance: Item
    """
    Call `use_item(Items.Weird_Substance)` on a bush to grow a maze, or on other plants to toggle their infection status.
    """

    Wood: Item
    """
    Obtained from bushes and trees.
    """




# -------------------------------------------------------------------------------
# Basic Types and Collections
# -------------------------------------------------------------------------------

# Section: Types




# -------------------------------------------------------------------------------
# Crop Management
# -------------------------------------------------------------------------------

# Section: Crops




# -------------------------------------------------------------------------------
# Movement
# -------------------------------------------------------------------------------

# Section: Crops




# -------------------------------------------------------------------------------
# Senses
# -------------------------------------------------------------------------------

# Section: Senses




# -------------------------------------------------------------------------------
# Megafarm
# -------------------------------------------------------------------------------

# Section: Megafarm




# -------------------------------------------------------------------------------
# Debug
# -------------------------------------------------------------------------------

# Section: Debug




# -------------------------------------------------------------------------------
# Auto Unlock
# -------------------------------------------------------------------------------

# Section: AutoUnlock




# -------------------------------------------------------------------------------
# Math
# -------------------------------------------------------------------------------

# Section: Math




# -------------------------------------------------------------------------------
# Utility
# -------------------------------------------------------------------------------

# Section: Utility




# -------------------------------------------------------------------------------
# Miscelaneous
# -------------------------------------------------------------------------------

# Section: Miscelaneous