from typing import Self, Any as _Any, overload
from collections.abc import Iterable, Callable
from builtins import (bool as _bool, int as _int, float as _float, str as _str,
					  range as _range,
					  tuple as _tuple, list as _list, set as _set, dict as _dict)

type Any = (
    _bool | _int | _float | _str | _range | # Python builtin    - basic types

	_tuple[Any] | _list[Any] |				# Python builtin    - collection types
    _set[Any] | _dict[Any, Any] |

	Direction | Entity | Entities | 		# Game builtins		- enum classes
    Ground | Grounds | Hat | Hats |
    Item | Items | Leaderboard |
    Leaderboards | Unlock | Unlocks |

	Drone |									# Game builtins		- megafarm classes

    None									# Python builtin	- None
)