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
