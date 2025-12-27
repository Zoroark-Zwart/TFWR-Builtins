import pathlib


CODE = "Code"
DOCSTRING = "Docstring"
DOCSTRING_COMMENT_BEGIN = '\t"""\n\t'
DOCSTRING_COMMENT_END = '\n\t"""\n'

TAG_SECTION = "# Section: "
TAG_DOCSTRING = "# Docstring: "

LABEL_DOCSTRING_OUTER = "# "
LABEL_DOCSTRING_INNER = "## "

SECTION_DIVIDER = "# -------------------------------------------------------------------------------"

def AddContributionsSection(templatecontent: list[str],
                            contributionsfile: str = pathlib.Path.cwd().joinpath("Template").joinpath("Contributions.py")
                            ) -> list[str]:
    NewTemplateContent = list()

    ContributionsContent = ""

    with open(contributionsfile) as FileContributions:
        ContributionsContent = FileContributions.read()

    for line in templatecontent:
        if line.find(TAG_SECTION + "Contributions") > -1:
            NewTemplateContent.append(ContributionsContent)
        else:
            NewTemplateContent.append(line)

    return NewTemplateContent

def CreateExample(examplecode: str):
    return NotImplementedError

def CreateUsedWith(usedwithlist: list[str]):
    return NotImplementedError

class Manager:
    Name: str
    Version: str
    Groupings: dict[str, dict[str, dict[str, str] | list[str]]]
    MergedContent: dict[str, list[str]]

    def __init__(self, name: str, version: str) -> None:
        self.Name = name
        self.Version = version
        self.Groupings = dict()
        self.MergedContent = dict()


    # function[list[dict[str, list[str]]]] <-- need to convert to proper type hint
    def __AddGrouping(self, groupingname: str, subname: str, parser) -> list[str]:
        GroupingDirectory = self.Version + "/" + subname + "/" + groupingname + "/"
        GroupingFiles = list()

        for group in pathlib.Path(GroupingDirectory).iterdir():
            if group.is_file():
                GroupingFiles.append(group)

        GroupingContent = parser(GroupingFiles)

        if not groupingname in self.Groupings:
            self.Groupings[groupingname] = dict()

        self.Groupings[groupingname][subname] = GroupingContent

        return GroupingContent

    def __ParserCode(self, groupfiles: list[str]) -> list[dict[str, list[str]]]:
        ParsedContent = list()

        for file in groupfiles:
            CollectSectionContentFlag = False
            SectionContent = list()

            with open(file) as FileParse:
                for line in FileParse:
                    if line.find(SECTION_DIVIDER) > -1:
                        if SectionContent:
                            ParsedContent.append(SectionContent)
                            SectionContent = list()

                        CollectSectionContentFlag = not CollectSectionContentFlag

                    if CollectSectionContentFlag:
                        SectionContent.append(line)

                ParsedContent.append(SectionContent)

        return ParsedContent

    def __ParserDocstring(self, groupfiles: list[str]) -> list[dict[str, list[str]]]:
        ParsedContent = dict()

        for file in groupfiles:
            SectionContent = ""

            with open(file) as FileParsed:
                BlockName = ""

                for line in FileParsed:
                    if line.find("#") > - 1:
                        if BlockName:
                            ParsedContent[BlockName] = SectionContent
                            SectionContent = ""

                        BlockName = line.strip("#").strip()
                    else:
                        SectionContent = SectionContent + line.strip("\n")

                ParsedContent[BlockName] = SectionContent

        return ParsedContent

    def AddGroupingCode(self, groupingname: str) -> list[str]:
        return self.__AddGrouping(groupingname, CODE, self.__ParserCode)


    def AddGroupingDocstring(self, groupingname: str) -> list[str]:
        return self.__AddGrouping(groupingname, DOCSTRING, self.__ParserDocstring)

    def MergeGroupings(self) -> list[str]:
        for group in self.Groupings:
            GroupCode = self.Groupings[group][CODE]
            GroupDocstring = self.Groupings[group][DOCSTRING]

            self.MergedContent[group] = list()
            MergedContentSection = self.MergedContent[group]

            for codesection in GroupCode:
                for codeline in codesection:
                    if codeline.find(TAG_DOCSTRING) > -1:
                        MergedContentSection.append(DOCSTRING_COMMENT_BEGIN + GroupDocstring[codeline.strip()[len(TAG_DOCSTRING):]] + DOCSTRING_COMMENT_END)
                    else:
                        MergedContentSection.append(codeline)

    def Compile(self, replacefile: bool = False,
                templatefile: str = pathlib.Path.cwd().joinpath("Template").joinpath("Template.py")
                ) -> str:
        CurrentFile = self.Name
        TemplateContent = list()

        with open(templatefile) as FileTemplate:
            for line in FileTemplate:
                TemplateContent.append(line)

        TemplateContent = AddContributionsSection(TemplateContent)

        if replacefile:
            CurrentFileBuffer = pathlib.Path(CurrentFile + ".py")
            if CurrentFileBuffer.exists():
                CurrentFileBuffer.unlink()
        else:
            FileCounter = None

            if pathlib.Path(CurrentFile + ".py").exists():
                FileCounter = 1

                while pathlib.Path(CurrentFile + f" ({FileCounter}).py").exists():
                    FileCounter = FileCounter + 1

            if FileCounter:
                CurrentFile = CurrentFile + f" ({FileCounter})"


        with open(CurrentFile + ".py", "a") as FileOutput:
            for templateline in TemplateContent:
                if templateline.find(TAG_SECTION) > -1:
                    Grouping = templateline[len(TAG_SECTION):].strip("\n").strip()
                    if Grouping in self.MergedContent:
                        for codeline in self.MergedContent[Grouping]:
                            FileOutput.write(codeline)
                    else:
                        FileOutput.write(templateline)
                else:
                    FileOutput.write(templateline)