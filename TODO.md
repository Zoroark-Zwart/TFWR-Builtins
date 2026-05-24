- Fill out a basic README
- Fill out a basic TODO
- Add basic test files for type hint completeness checking
- Add Official builtins file for 1.0

- Update signature for: `def len(object : string | _dict[_Hashable_, _Any_] | _list[_Any_] | _set[_Hashable_] | _tuple[_Any_,...]) -> _int:`

Templates/BuiltinsBuilder:

- Add remaining type hints
- Add documentation
- Add helper functions to help with creating more docstring snippets
- Add an overload constructor option to allow for copying of a given Manager object







Other code

`type _AnyCollection = (
	_tuple[AnyTFWR,...] |

	dict[_int, AnyTFWR] | _dict[_int, AnyTFWR] |
	dict[_float, AnyTFWR] | _dict[_float, AnyTFWR] |
	dict[string, AnyTFWR] | _dict[string, AnyTFWR] |
	dict[None, AnyTFWR] | _dict[None, AnyTFWR] |

	set[_int] | _set[_int] |
	set[_float] | _set[_float] |
	set[string] | _set[string] |
	set[None] | _set[None] |

	list[_int] | _list[_int] |
	list[_float] | _list[_float] |
	list[string] | _list[string] |
	list[None] | _list[None] |

	list[Entity] | _list[Entity] |
	list[Entities] | _list[Entities] |
	list[Ground] | _list[Ground] |
	list[Grounds] | _list[Grounds] |
	list[Hat] | _list[Hat] |
	list[Hats] | _list[Hats] |
	list[Item] | _list[Item] |
	list[Items] | _list[Items] |
	list[Leaderboard] | _list[Leaderboard] |
	list[Leaderboards] | _list[Leaderboards] |
	list[Unlock] | _list[Unlock] |
	list[Unlocks] | _list[Unlocks] |


	dict[Entity, AnyTFWR] | _dict[Entity, AnyTFWR] |
	dict[Entities, AnyTFWR] | _dict[Entities, AnyTFWR] |
	dict[Ground, AnyTFWR] | _dict[Ground, AnyTFWR] |
	dict[Grounds, AnyTFWR] | _dict[Grounds, AnyTFWR] |
	dict[Hat, AnyTFWR] | _dict[Hat, AnyTFWR] |
	dict[Hats, AnyTFWR] | _dict[Hats, AnyTFWR] |
	dict[Item, AnyTFWR] | _dict[Item, AnyTFWR] |
	dict[Items, AnyTFWR] | _dict[Items, AnyTFWR] |
	dict[Leaderboard, AnyTFWR] | _dict[Leaderboard, AnyTFWR] |
	dict[Leaderboards, AnyTFWR] | _dict[Leaderboards, AnyTFWR] |
	dict[Unlock, AnyTFWR] | _dict[Unlock, AnyTFWR] |
	dict[Unlocks, AnyTFWR] | _dict[Unlocks, AnyTFWR] |

	set[Entity] | _set[Entity] |
	set[Entities] | _set[Entities] |
	set[Ground] | _set[Ground] |
	set[Grounds] | _set[Grounds] |
	set[Hat] | _set[Hat] |
	set[Hats] | _set[Hats] |
	set[Item] | _set[Item] |
	set[Items] | _set[Items] |
	set[Leaderboard] | _set[Leaderboard] |
	set[Leaderboards] | _set[Leaderboards] |
	set[Unlock] | _set[Unlock] |
	set[Unlocks] | _set[Unlocks]
)`


`type _AnyCollection = (
	tuple[AnyTFWR, ...] |
	_list[AnyTFWR] | _set[AnyTFWR] | _dict[Hashable, AnyTFWR] |		# Python builtins
    list[AnyTFWR] | set[AnyTFWR] | dict[Hashable, AnyTFWR]			# game builtins
)`

Old stuff to maybe add back for `__builtins__`:

`_Hashable_ = TypeVar("_Hashable_", Hashable, Hashable, covariant = True)`
`_Any_ = TypeVar("_Any_", AnyTFWR, AnyTFWR, covariant = True)`



Maybe:

```
class str: # now, this is a problem. how do i limit methods while accepting string literals? there's no typing.Str to help me like with the others
    """\
returns a string representation of object.

takes 1 ticks to execute.

example:
string = str(1000)"""

    def __init__(self, object: _Optional[_Any] = None) -> None: ...
    def __iter__(self) -> _Iterator[Str]: ...
    def __len__(self) -> int: ... # still annoying

    def __eq__(self, value: object) -> bool: ...
    def __lt__(self, other: Str) -> bool: ...
    def __gt__(self, other: Str) -> bool: ...
    def __le__(self, other: Str) -> bool: ...
    def __ge__(self, other: Str) -> bool: ...

    def __add__(self, other: Str) -> Str: ...
    def __iadd__(self, other: str) -> Str: ...

    def print(self, *args: _Any) -> None: # just for the sake of it, if someone wants
        """\
        Prints all args into the air above the drone using smoke. This action is not affected by speed upgrades.
        Multiple values can be printed at once.

        returns None

        takes 1s to execute.

        example:
        print("ground:", get_ground_type())"""

    def quick_print(self, *args: _Any) -> None:
        """\
        Prints a value just like print(*args) but it doesn't stop to write it into the air so it can only be found on the output page.

        returns None

        takes 0 ticks to execute.

        example:
        quick_print("hi mom")"""
```