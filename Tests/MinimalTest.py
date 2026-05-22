from Release.__builtins__minimal import *
#  from __builtins__ import *

from collections.abc import Iterator as _Iterator
from typing import Self

class GroundsClass:
    def __init__(self) -> None:
        pass

    def __iter__(self: Self) -> _Iterator[Ground]:
        ...

    def __next__(self: Self) -> Ground:
        ...

    Grassland: Ground
    """
    The default ground. Grass will automatically grow on it.
    """

    Soil: Ground
    """
    Calling `till()` turns the ground into this. Calling `till()` again changes it back to grassland.
    """

# Grounds = GroundsClass()

TestDict: dict[Hashable, int] = dict()
TestList: list[dict[Hashable, int]] = list()
for ground in Grounds:
    TestDict[ground] = 1
    TestList.append(TestDict)




print(Grounds.Grassland)
