# May/26 Update 2

- Added updated `spawn_drone` example documentation
- `None` note clarifications

# May/26 Update 1

- Generalized `V` in `list` custom type to `Any` since it still causes typing errors
- Allowed `list` custom type constructor to accept tuples of any size
- Removed `None` as a return type from all functions that return it from type hints  to reduce complexity in type hints due to lack of type casts. Added notes about this lack of type hint where applicable.
- Document rework

# May/25 Update 1

- Exposed more commonly useful types to make them available
- Reverted some private types to public
- Added more import explanations
- Organized imports
- Added credit for @Rat
- Added additional comment on how `spawn_drone` passes arguments
- Removed unneeded enum method from enum classes
- Added `WorldSizes` literals to return of `get_world_size`

# May/24 Update 2

- Reverted `_AnyCollection_` to the less specific version and settled it not being a true Any but instead a "these are all types that TFWR can support match one of them"
- Made `list` `V` more specific as AnyTFWR
- Made `dict` `K` more general as Any
- Made `Drone` `R` more general as Any

# May/24 Update 1

- Added better documentation for custom types catch-alls
- Added `_range` as a valid type in all appropriate places taking the place of `builtins.range` when `range_class` is defined as a custom type

# May/23 Update 5

- Removed `TypeVar` import
- Changed `DictType`, `ListType`, `SetType`, and `RangeType` to `SomethingTFWR`
- Moved `Self` to private import
- Minimized vertical spacing for custom types

# May/23 Update 4

- Fixed protocol of `has_finished`
- Added custom types for functions with complex return types to help type hint them. These are just the main function word capitalized. Included: `Measure`, `Cost`, `Companion`
- `Drone` and `Entity` left out to maintain that they can return return `None` when hovered.
- Spelling error fixes

# May/23 Update 3

- Added overloads for `min` and `max` to properly catch all possibilities of valid uses of those functions.

# May/23 Update 2

- Gave default value to `index` of list `pop`
- Added new definition header to `spawn_drone` that checks that the provided argument types match the parameter types in the task function, and added `None` to return type
- Disabled the ability to pass in keyword arguments to all functions that take arguments
- Removed `Item` and `Items` from types of `thing` in `get_cost`
- Changed return value of `get_cost` to: `dict[Item, _int] | _dict[Item, _int] | dict[_Never, _Never]`
- Removed lingering `int | float` and replaced with `float`
- Made `Iterator` as a pass-through type
- Added Enum plurals to crop functions
- Changed default value of `level` of `get_cost` to 0
- Changed documentation to match type changes
- Spelling error fixes
- Added `WorldSize` type that is a literal from 3-32
- Added a literal constraint to `size` to `WorldWizes` of `set_world_size`

# May/23 Update 1

- Added `DictType`, `ListType`, `SetType` and `RangeType` as a catch-all for custom types and Python builtin types
- Added the `contains` dunder with comparison restrictions to all custom types

# May/21 Update 8

- Made `V` type var of custom list and `K` of custom dicts be generic Any in order to be flexible enough for compatibility
- Changed UFCS functions of similar type to use generic Any as well for compatibility
- Made the constructor `input` parameter except `Iterable[V]` for custom list and `Iterable[K]` for custom set
- Changed `_AnyCollection` from `Hashable` keys to a explicit list of keys to help with compatibility to an Any type

# May/21 Update 7

- Moved docstring for `Primitive` to below the custom type instead of on top of it

# May/21 Update 6

- Specified more direct functionality for custom classes `list`, `dict`, `set`
- Generalized using type variables
- Adjusted UFCS versions to use the type variables from the custom classes
- Made an overload for `pop` since it did not play well being mixed
- Added a custom class for `range_class` with special game-only functionality
- Updated docstrings where applicable
- Changed `AnyTFWR` and `AnyIterable` to take from `_AnyCollection` which defines `builtin` collections and game collections
- Imports adjusted to note the new custom class and added `_Iterator`
- Added warning in description for custom class about assignability.

# May/21 Update 5

- Renamed `Any` to `AnyTFWR`
- Unaliased `builtins.Any` and let it be just `Any`
- Changes made to make it distinguishable which type of Any is being used in all scenarios

# May/21 Update 4

- Changed `Drone` to `Drone[Any]` for parameter `drone` of `has_finished`
- Changed `Drone` to `Drone[Any]` in custom type `Hashable`
- Changed `object` of `str` to use `builtins.Any` (alias `_Any`) to make it purely generic

# May/21 Update 3

- Renamed `ReturnType` to `R` in `Drone` class
- Added `ModuleType` to custom type `Any`
- Added `Items` as type for `item` parameter for `num_items`
- Change `Drone` to `Drone[Any]` in `Any` custom type

# May/21 Update 2

- Added `None` return type UFCS functions
- Removed `return Class()` from all Enum classes
- Added `range_class` as accepted `object` types in `len`

# May/21 Update 1

- Added return type to Drone class
- Updated TODO

# Apr/08 Update 1

- Reverted changes for Enum class variables to use the specific singular Enum version instead of `_auto()` because auto creates a literal of that singular class, which can cause typing confusion when the singular class is also available as a type

The Enum classes are still iterable because of `_generate_next_value_`. Since the code is not meant to be run outside of the game, there is no need to have usable Enums when iterating over them.

- Adjusted the unlock functions: `get_cost`, and `unlock` to accept the enumerated version and the specific version of an Enum. `num_unlocked` is changed to use the custom `Enums` type to save on column length. The docstring explains which of those is acceptable.

This allows for stuff like:

`for hat in Hats:
  num_unlocked(hat)`

To not throw typing errors.

- Rearranged the `Enums` and `Any` custom types so that `Direction` is not a part of `Enums`. Since `Direction` acts more like a regular object. Stuff like `num_unlocked` doesn't accept a `Direction` as well.

# Apr/07 Update 1

- Made custom classes optional as they can cause conflicts when using `[]` to initialize an empty list, `{}` to initialize a dict, and when trying to initialize with list, dict, and set literals. Added some comments to note why these classes are there.
- Added a comment explaining the method-as-function section
- Added new custom types for Primitives, Any and Hashable with comments explaining them
- Added some type safety Sequence and Container to functions that accept a list, set, dict, or tuple for type checkers that may complain about collections of the custom types.
- Created a type alias for str -> string and range -> range_class to allow type hints where those types are shadowed by in-game functions
- Added notes about these aliases in the game function docstring
- Changed the dict in `get_cost` to use the type alias `_dict` instead of the potential custom class `dict` for compatibility
- Changed parameter types for `print` and `quick_print` to `_Any` (builtins.Any from Python) to handle possible unknown typings and very complex unknowable types.
- Changed from using Sequence and Container to using covariant type vars in functions that a list, dict, or set of Any or Hashable
- Changed builtin enums to use Python's enum.Enum class for better iteration

# Mar/24 Update 1

- Improved `simulate` typing and documentation in Minimal
- Corrected tick cost calculation and example errors for `remove` and `list.remove` in Minimal
- Fixed tagging for enums to help avoid possible conflicts with names and to future proof conflicts a bit in Minimal

# Mar 8/26 Update 1

- Added some experimentation for custom classes and Any type to Tests/TypingRecognition_Minimal.py
- Type classes type parameter refinements in Minimal/Code/Types/TypeClasses.py
- Corrected parameter of add in Minimal/Code/Types/TypeFunctions.py
- Corrected index and object parameters for insert in Minimal/Code/Types/TypeClasses.py and Minimal/Docstring/Types/TypeFunctions.py
- Added custom Any type that only includes Python builtin basic and collection types and game builtin types
- Added Minimal/Code/Megafarm/MegafarmClasses.py and Minimal/Docstring/Megafarm/MegafarmClasses.md
- Added Drone type to Minimal and updated/amended Megafarm Docstrings
- Fixed return type of has_finished to a bool
- Updated simulate function signature
- Renamed IterableCollections to AnyIterable in Minimal/Code/Types/TypeClasses.py
- Added a dedicated Template/Imports.py file for imports and changed template to match

# Mar 7/26 Update 1

- Changed tick cost for get_time in Minimal
- Changed parameter name for spawn_drone from callback to task in Minimal
- Fixed Docstring tag in Minimal/Code/Movement/MovementFunctions.py
- Added type ignore to range overloads to avoid needing to implement them as they are not needed
- Added type arguments to dict, list and set in Minimal/Code/Types/TypesClasses.py
- Added Self typing import in Template/Template.py to be used for new custom classes
- Mostly added custom class definitions for dict, list and set that contain only the methods usable in-game to Minimum
- Added function versions of add, append, insert, pop, and removed in Minimal
- Sorted order of type functions in Minimal
- Fixed Docstring for get_pos_x

# Feb 24/26 Update 2

- Added pyrightconfig.json to help with typing error reduction and to help change modes for future use. Especially useful for test scripts.
- Renamed Tests/TypingRecognition.py to Tests/TypingRecognition_Minimal.py
- - Added a bit more test coverages

# Feb 24/26 Update 1

- Added all Code and Docstring files for a complete Minimal build
- Added some additions and fixes that aren't present in the current official builtins file
- Changed range() so that it now has 3 different overloads and appropriate comment
- Changed the wording of some example usages to avoid using comments inside of the examples. Instead, made those examples all print something and added an "Output" section
- Added dummy default class overrides for dict, list, and set to help in the future. More should follow
- Added alias names for primitive types to avoid collisions in the future
- Adjusted spawn_drone to accept a callable with no arguments
- Adjusted Template/BuiltinsBuilder.Manager.\_\_ParserDocstring to output a list of the contents instead of a string. Also added content compilation detection to safely allow newlines inside of the content itself
- Adjusted Template/BuiltinsBuilder.Manager.MergeGroupings to now accept a list for docstring content and adding appropriate padding to each new line
- Reworked spacing in Template/Template.py
- Added overload support to Template/Template.py
- Added Tests/TypingRecognition.py to help test functionality. Should expand this

# Dec 28/25 Update 1

- Refactored some variable names to help make them clearer

# Dec 27/25 Update 1

- Renamed Changelog.md to CHANGELOG.md
- Added TODO.md and some tasks
- Added Release folder and changed Template/BuiltinsBuilder. Compile to output to Release
- Changed Template/BuiltinsBuilder.AddContributionsSection to be a bit more direct but still non-destructive
- Refactored some variable names to help make them clearer
- Changed Template/BuiltinsBuilder.Compile to not output sections tags unless it has content for it
- Changed Template/BuiltinsBuilder.Compile so that it now returns the output contents
- Changed Template/BuiltinsBuilder.Compile to add newline padding after a section
- Changed Template/Template.py to remove some newlines to account for the automatic insertion of new lines from section padding
- Changed Template/BuiltinsBuilder.MergeGroupings to return the merged content
- Changed Template/BuiltinsBuilder.MergeGroupings to result Changed Template/BuiltinsBuilder.Groups to an empty dict
- Added Template/Descriptive.py as continuation of the Minimal template
- Added Template/BuiltinsBuilder setter and getters for name and version to allow renaming of template names and versions during continuance files
- Added Template/BuiltinsBuilder.Manager.TYPE_GROUPING types for code, docstring, and merged
- Updated Template/BuiltinsBuilder.Manager fields to be marked as private intention
- Separated Template/BuiltinsBuilder.Manager.Groupings types into more comprehensible code type and docstring type
- Changed Template/BuiltinsBuilder.Manager.TYPE_GROUPING_CODE to include a dictionary based on section name (ie Items, Hats, etc.)
- Added and reworked Template/BuiltinsBuilder constants to help with formatting decisions

# Dec 26/25 Update 4

- Starting from this update the date has been corrected

# Dec 25/25 Update 3

- Changed padding in BuiltinsBuilder.MergeGroupings to use relative padding parsed from the provided code file

# Dec 25/25 Update 2

- Fixed a docstring tag type for Item in Template/Items.py
- Renamed Template/BuiltinsManager.py to Template/BuiltinsBuilder.py
- Renamed Template/BuiltinsMinimal.py to Template/Minimal.py
- Changed Template/BuiltinsBuilder.\_\_AddGroupings to use a provided file parser
- Added constants to Template/BuiltinsBuilder representing different strings and tags used in code and docstrings files
- Added an implementation for Template/BuiltinsBuilder.MergeGroupings and Template/BuiltinsBuilder.Compile
- Updated Template/Minimal.py to use the new implementations and test prints
- Updated Template/Template.py to use Template/BuiltinsBuilder.TAG_SECTION in places meant to be replaced by a certain section
- Converted to pathlib from os
- Added BuiltinsBuilder.AddContributionsSection to add in contributions for template files
- Added stubs for BuiltinsBuilder.CreateExample and BuiltinsBuilder.CreateUsedWith as helper files to help create snippets of docstrings
  - Should add more of these later and implement

# December 26th, 2025

- Added basic root structure
- Added example version structure to Minimal
- Added example file for Minimal/Code/Items.py and Minimal/Docstring/Items.md
- Created a starting template file under Template/Template.py
- Added contributions under Template/Contributions.py
- Created basic class for managing builtin file compilation and creation under Template/BuiltinManager.py
- Created entry point for the Minimal version under Template/CreateMinima.py
- Added basic gitignore
