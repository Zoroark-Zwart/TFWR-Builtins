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
- Type classes type paramter refinements in Minimal/Code/Types/TypeClasses.py
- Corrected paramenter of add in Minimal/Code/Types/TypeFunctions.py
- Corrected index and object paramters for insert in Minimal/Code/Types/TypeClasses.py and Minimal/Docstring/Types/TypeFunctions.py
- Added custom Any type that only includes Python builtin basic and collection types and game builtin types
- Added Minimal/Code/Megafarm/MegafarmClasses.py and Minimal/Docstring/Megafarm/MegafarmClasses.md
- Added Drone type to Minimal and updated/ammended Megafarm Docstrings
- Fixed return type of has_finished to a bool
- Updated simulate function signature
- Renamed IterableCollections to AnyInterable in Minimal/Code/Types/TypeClasses.py
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
- Changed range() so that it now has 3 different overloads and appropriate commment
- Changed the wording of some example usages to avoid using comments inside of the examples. Instead, made those examples all print something and added an "Output" section
- Added dummy default class overrides for dict, list, and set to help in the future. More should follow
- Added alias names for primitive types to avoid collisions in the future
- Adjusted spawn_drone to accept a callable with no arguments
- Adjusted Template/BuiltinsBuilder.Manager.\_\_ParserDocstring to output a list of the contents instead of a string. Also added content compliation detection to safely allow newlines inside of the content itself
- Adjusted Template/BuiltinsBuilder.Manager.MergeGroupings to now accept a list for docstring content and adding appropriate padding to each new line
- Reworked spacing in Template/Template.py
- Added overload support to Template/Template.py
- Added Tests/TypingRecognition.py to help test functionality. Should expand this

# Dec 28/25 Update 1

- Refactored some variable names to help make them clearer

# Dec 27/25 Update 1

- Renamed Changelog.md to CHANGELOG.md
- Added TODO.md and some tasks
- Added Release folder and changed Template/BuiltinsBuilder.Compile to ouput to Release
- Changed Template/BuiltinsBuilder.AddContributionsSection to be a bit more direct but still non-destructive
- Refactored some variable names to help make them clearer
- Changed Template/BuiltinsBuilder.Compile to not output sections tags unless it has content for it
- Changed Template/BuiltinsBuilder.Compile so that it now returns the output contents
- Changed Template/BuiltinsBuilder.Compile to add newline padding after a section
- Changed Template/Template.py to remove some newlines to account for the automatic insertion of new lines from section padding
- Changed Template/BuiltinsBuilder.MergeGroupings to return the merged content
- Changed Template/BuiltinsBuilder.MergeGroupings to result Changed Template/BuiltinsBuilder.Groups to an empty dict
- Added Template/Descriptive.py as continuation of the Minimal template
- Added Template/BuiltinsBuilder setter and getters for name and version to allow renaming of template names and versions during continance files
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
- Created basic class for managing builtin file compliation and creation under Template/BuiltinManager.py
- Created entry point for the Minimal version under Template/CreateMinima.py
- Added basic gitignore
