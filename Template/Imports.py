# Expose some useful types to allow for typing without using a typing import.
# Typing imports would fail to run in-game as they are not ignored.

# Notes on aliases because of TFWR functions:
# - string -> builtins.str
# - range_class -> builtins.range

from typing import Self, TypeVar, Literal, Final, overload
from collections.abc import Callable, Iterable, Sequence, Container

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
    bool as _bool, int as _int, float as _float,
    tuple as _tuple, list as _list, set as _set, dict as _dict
)
from collections.abc import Iterator as _Iterator

from types import ModuleType
from typing import Any
from enum import Enum as _Enum