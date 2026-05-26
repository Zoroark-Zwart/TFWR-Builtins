# Expose some useful types to allow for typing without using a typing import.
# Typing imports would fail to run in-game as they are not ignored.
# Ignore any type warnings as needed by your environment.
# Some types are provided as private to the let file have control
# over the regular defaults and are not commonly useful for typing most code

# Notes on aliases because of TFWR functions:
# - string -> builtins.str
# - range_class -> builtins.range

# Note: `None` is not type hinted in optional return types to reduce typing complexity due to lack of type casts. This affects these functions:
# - `measure`
# - `get_companion`
# - `get_cost`
# - `spawn_drone`
# Documentation for `None` return type is available for when running the code in-game

from typing import (
    Any, Literal, Final,
    overload, Self, Never
)
from collections.abc import (
    Callable, Iterator, Iterable,
    Sequence, Container, Collection
)
from types import ModuleType

from builtins import (
    bool, int, float, str as string,
    tuple,

    # If you uncomment the custom classes found below then
    # comment this line to prevent conflicts
    range as range_class,
    list, set, dict
)

# Used for when the builtin type is desirable over a possible
# redefinition using the same name
from builtins import (
    bool as _bool, int as _int, float as _float, range as _range,
    tuple as _tuple, list as _list, set as _set, dict as _dict
)
from enum import Enum as _Enum