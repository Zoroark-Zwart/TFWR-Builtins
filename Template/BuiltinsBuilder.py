import pathlib


CODE = "Code"
DOCSTRING = "Docstring"
DOCSTRING_COMMENT_BEGIN = '"""\n'
DOCSTRING_COMMENT_END = '"""\n'

TAG_SECTION = "# Section: "
TAG_DOCSTRING = "# Docstring: "

LABEL_DOCSTRING_OUTER = "# "
LABEL_DOCSTRING_INNER = "## "

SECTION_DIVIDER = "# -------------------------------------------------------------------------------"
SECTION_PADDING = "\n\n"

SECTION_SUB_DIVIDER = "# --------------------------------------------------"

CATEGORY_PADDING = "\n\n"

def AddContributionsSection(templatecontent: list[str],
                            contributionsfile: str = pathlib.Path.cwd()
                                .joinpath("Template")
                                .joinpath("Contributions.py")
                            ) -> list[str]:
    NewTemplateContent = list(templatecontent)

    ContributionsContent = ""

    with open(contributionsfile) as FileContributions:
        ContributionsContent = FileContributions.read()

    for i in range(len(NewTemplateContent)):
        if NewTemplateContent[i].find(TAG_SECTION + "Contributions") > -1:
            NewTemplateContent[i] = ContributionsContent
            break

    return NewTemplateContent

def AddImportsSection(templatecontent: list[str],
                            importsfile: str = pathlib.Path.cwd()
                                .joinpath("Template")
                                .joinpath("Imports.py")
                            ) -> list[str]:
    NewTemplateContent = list(templatecontent)

    ImportsContent = ""

    with open(importsfile) as FileImports:
        ImportsContent = FileImports.read()

    for i in range(len(NewTemplateContent)):
        if NewTemplateContent[i].find(TAG_SECTION + "Imports") > -1:
            NewTemplateContent[i] = ImportsContent
            break

    return NewTemplateContent

def CreateExample(examplecode: str) -> str:
    return NotImplementedError

def CreateUsedWith(usedwithlist: list[str]) -> str:
    return NotImplementedError

class Manager:
    type TYPE_GROUPING_CODE = dict[str, list[str]]
    type TYPE_GROUPING_DOCSTRING = dict[str, dict[str, str]]
    type TYPE_GROUPING_MERGED = dict[str, list[str]]

    __Name: str
    __Version: str
    __Groupings: dict[str, TYPE_GROUPING_CODE | TYPE_GROUPING_DOCSTRING]
    __MergedContent: TYPE_GROUPING_MERGED

    def __init__(self, name: str, version: str) -> None:
        self.SetName(name)
        self.SetVersion(version)
        self.__Groupings = dict()
        self.__MergedContent = dict()

    # Does an iter method make sense?
    # Better alternative to returning a compile string from respective method? Or a merge dict?
    def __iter__(self):
        return NotImplementedError

    def SetName(self, newname: str) -> None:
        self.__Name = newname

    def GetName(self) -> str:
        return self.__Name

    def SetVersion(self, newversion: str) -> None:
        self.__Version = newversion

    def GetVersion(self) -> str:
        return self.__Version

    # function[list[dict[str, list[str]]]] <-- need to convert to proper type hint
    def __AddGrouping(self, groupingname: str, subname: str, parser) -> TYPE_GROUPING_CODE | TYPE_GROUPING_DOCSTRING:
        GroupingDirectory = self.__Version + "/" + subname + "/" + groupingname + "/"
        GroupingFiles = list()

        for group in pathlib.Path(GroupingDirectory).iterdir():
            if group.is_file():
                GroupingFiles.append(group)

        GroupingContent = parser(GroupingFiles)

        if not groupingname in self.__Groupings:
            self.__Groupings[groupingname] = dict()

        self.__Groupings[groupingname][subname] = GroupingContent

        return GroupingContent

    def __ParserCode(self, groupfiles: list[str]) -> TYPE_GROUPING_CODE:
        ParsedContent = dict()

        for file in groupfiles:
            CollectSectionContentFlag = False
            SectionContent = list()

            with open(file) as FileParse:

                # This is probably not the best way to do this, but I wanted a way that was not platform specific and this looked like it could work like that.
                # If I find a better way this will be updated.
                SectionName = file.name[:-4]

                for line in FileParse:
                    if line.find(SECTION_DIVIDER) > -1:
                        if SectionContent:
                            ParsedContent[SectionName] = SectionContent
                            SectionContent = list()

                        CollectSectionContentFlag = not CollectSectionContentFlag

                    if CollectSectionContentFlag:
                        SectionContent.append(line)

                ParsedContent[SectionName] = SectionContent

        return ParsedContent

    def __ParserDocstring(self, groupfiles: list[str]) -> TYPE_GROUPING_DOCSTRING:
        ParsedContent = dict()

        for file in groupfiles:
            SectionContent = list()
            ContentCompilingFlag = False

            with open(file) as FileParse:
                BlockName = ""

                for line in FileParse:
                    if line.find("#") > - 1:
                        if BlockName:
                            ParsedContent[BlockName] = SectionContent[:-1] # Remove last blank line from markdown
                            SectionContent = list()
                            ContentCompilingFlag = False

                        BlockName = line.strip("#").strip()
                    else:
                        # Treat blank lines as inside of the actual comment body as valid content
                        if ContentCompilingFlag:
                            if line != "\n":
                                SectionContent.append(line.strip("\n"))
                            else:
                                SectionContent.append("")

                        # Remove first blank line from markdown
                        if not ContentCompilingFlag and line == "\n":
                            ContentCompilingFlag = True

                ParsedContent[BlockName] = SectionContent

        return ParsedContent

    def AddGroupingCode(self, groupingname: str) -> TYPE_GROUPING_CODE:
        return self.__AddGrouping(groupingname, CODE, self.__ParserCode)


    def AddGroupingDocstring(self, groupingname: str) -> TYPE_GROUPING_DOCSTRING:
        return self.__AddGrouping(groupingname, DOCSTRING, self.__ParserDocstring)

    def MergeGroupings(self) -> TYPE_GROUPING_MERGED:
        for group in self.__Groupings:
            GroupCode = self.__Groupings[group][CODE]
            GroupDocstring = self.__Groupings[group][DOCSTRING]

            self.__MergedContent[group] = list()
            MergedContentSection = self.__MergedContent[group]

            for codesection in GroupCode:
                for codeline in GroupCode[codesection]:
                    if codeline.find(TAG_DOCSTRING) > -1:
                        Padding = codeline[:codeline.find("#")]

                        SectionComment = Padding + DOCSTRING_COMMENT_BEGIN

                        for docline in GroupDocstring[codeline.strip()[len(TAG_DOCSTRING):]]:
                            SectionComment = SectionComment + Padding + docline + "\n"

                        SectionComment = SectionComment + Padding + DOCSTRING_COMMENT_END

                        MergedContentSection.append(SectionComment)
                    else:
                        MergedContentSection.append(codeline)

                MergedContentSection.append("\n\n")

        self.__Groupings = dict()

        return self.__MergedContent

    def Compile(self, replacefile: bool = False,
                templatefile: str = pathlib.Path.cwd().joinpath("Template").joinpath("Template.py")
                ) -> str:
        CurrentFileName = self.__Name
        TemplateContent = list()

        with open(templatefile) as FileTemplate:
            for line in FileTemplate:
                TemplateContent.append(line)

        TemplateContent = AddContributionsSection(TemplateContent)
        TemplateContent = AddImportsSection(TemplateContent)

        ReleaseDirectory = pathlib.Path("Release")

        if replacefile:
            CurrentFileBuffer = ReleaseDirectory.joinpath(CurrentFileName + ".py")

            if CurrentFileBuffer.exists():
                CurrentFileBuffer.unlink()
        else:
            FileCounter = None

            if ReleaseDirectory.joinpath(CurrentFileName + ".py").exists():
                FileCounter = 1

                while ReleaseDirectory.joinpath(CurrentFileName + f" ({FileCounter}).py").exists():
                    FileCounter = FileCounter + 1

            if FileCounter:
                CurrentFileName = CurrentFileName + f" ({FileCounter})"


        with open(ReleaseDirectory.joinpath(CurrentFileName + ".py"), "a") as FileOutput:
            for templateline in TemplateContent:
                if templateline.find(TAG_SECTION) > -1:
                    Grouping = templateline[len(TAG_SECTION):].strip("\n").strip()

                    if Grouping in self.__MergedContent:
                        for codeline in self.__MergedContent[Grouping]:
                            FileOutput.write(codeline)

                    FileOutput.write(SECTION_PADDING)
                else:
                    FileOutput.write(templateline)

        with open(ReleaseDirectory.joinpath(CurrentFileName + ".py"), "r") as FileOutput:
            OutputContent = FileOutput.read()

        return OutputContent