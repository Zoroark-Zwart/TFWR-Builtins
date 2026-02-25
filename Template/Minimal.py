import BuiltinsBuilder

BuiltinsManager: BuiltinsBuilder.Manager = BuiltinsBuilder.Manager("__builtins__minimal", "Minimal")

BuiltinsManager.AddGroupingCode("Enums")
BuiltinsManager.AddGroupingDocstring("Enums")

BuiltinsManager.AddGroupingCode("Types")
BuiltinsManager.AddGroupingDocstring("Types")

BuiltinsManager.AddGroupingCode("Crops")
BuiltinsManager.AddGroupingDocstring("Crops")

BuiltinsManager.AddGroupingCode("Movement")
BuiltinsManager.AddGroupingDocstring("Movement")

BuiltinsManager.AddGroupingCode("Senses")
BuiltinsManager.AddGroupingDocstring("Senses")

BuiltinsManager.AddGroupingCode("Megafarm")
BuiltinsManager.AddGroupingDocstring("Megafarm")

BuiltinsManager.AddGroupingCode("Debug")
BuiltinsManager.AddGroupingDocstring("Debug")

BuiltinsManager.AddGroupingCode("Unlock")
BuiltinsManager.AddGroupingDocstring("Unlock")

BuiltinsManager.AddGroupingCode("Math")
BuiltinsManager.AddGroupingDocstring("Math")

BuiltinsManager.AddGroupingCode("Utility")
BuiltinsManager.AddGroupingDocstring("Utility")

BuiltinsManager.AddGroupingCode("Miscelaneous")
BuiltinsManager.AddGroupingDocstring("Miscelaneous")

# print(BuiltinsManager._Manager__Groupings)

if __name__ == "__main__":
    BuiltinsManager.MergeGroupings()

    # print(BuiltinsManager._Manager__MergedContent)

    # for grouping in BuiltinsManager._Manager__MergedContent:
    #     for line in BuiltinsManager._Manager__MergedContent[grouping]:
    #         print(line)

    BuiltinsManager.Compile(True)