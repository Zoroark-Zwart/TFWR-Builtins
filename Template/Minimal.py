import BuiltinsBuilder

BuiltinsMinimal = BuiltinsBuilder.Manager("__builtins__minimal", "Minimal")

BuiltinsMinimal.AddGroupingCode("Enums")
BuiltinsMinimal.AddGroupingDocstring("Enums")

# print(BuiltinsMinimal.Groupings)

BuiltinsMinimal.MergeGroupings()

# for grouping in BuiltinsMinimal.MergedContent:
#     for line in BuiltinsMinimal.MergedContent[grouping]:
#         print(line)

BuiltinsMinimal.Compile(True)
