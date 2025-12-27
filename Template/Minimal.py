import BuiltinsBuilder

BuiltinsManager: BuiltinsBuilder.Manager = BuiltinsBuilder.Manager("__builtins__minimal", "Minimal")

BuiltinsManager.AddGroupingCode("Enums")
BuiltinsManager.AddGroupingDocstring("Enums")

# print(BuiltinsManager._Manager__Groupings)

if __name__ == "__main__":
    BuiltinsManager.MergeGroupings()

    # print(BuiltinsManager._Manager__MergedContent)

    # for grouping in BuiltinsManager._Manager__MergedContent:
    #     for line in BuiltinsManager._Manager__MergedContent[grouping]:
    #         print(line)

    BuiltinsManager.Compile(True)