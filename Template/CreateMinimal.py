from BuiltinManager import *

BuiltinsMinimal = BuiltinManager("__builtins__minimal.py", "Minimal")

print(BuiltinsMinimal.AddGroupingCode("Enums"))
print(BuiltinsMinimal.AddGroupingDocstring("Enums"))

print(BuiltinsMinimal.Groupings)