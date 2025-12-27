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
