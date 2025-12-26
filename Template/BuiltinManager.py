import os

class BuiltinManager:
    Name: str
    Version: str
    Groupings: dict[str, dict[str, list[str]]]

    def __init__(self, name: str, version: str) -> None:
        self.Name = name
        self.Version = version
        self.Groupings = dict()


    def __AddGrouping(self, groupingname: str, subname: str) -> list[str]:
        GroupingDirectory = self.Version + "/" + subname + "/" + groupingname + "/"
        GroupingFiles = os.listdir(GroupingDirectory)
        GroupingContents = list()

        for file in GroupingFiles:
            with open(GroupingDirectory + file) as FileOpened:
                GroupingContents.append(FileOpened.read())

        if not groupingname in self.Groupings:
            self.Groupings[groupingname] = dict()

        self.Groupings[groupingname][subname] = GroupingContents

        return GroupingContents

    def AddGroupingCode(self, groupingname: str) -> list[str]:
        return self.__AddGrouping(groupingname, "Code")


    def AddGroupingDocstring(self, groupingname: str) -> list[str]:
        return self.__AddGrouping(groupingname, "Docstring")

    def MergeGroupings(self):
        ...

    def Compile(self) -> str:
        ...