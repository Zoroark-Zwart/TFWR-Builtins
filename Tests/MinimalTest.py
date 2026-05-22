from Release.__builtins__minimal import *
#  from __builtins__ import *

import builtins

TestDict: dict[int, int] = dict()
# TestDict = dict({1:1})
TestDict2: dict[int, int] = dict(TestDict)

TestList: list[int] = list(TestDict)
TestList2: list[tuple[int,int]] = list({(1,2):1})
TestList6: list[dict[int, int] | builtins.dict[int, int]] = list()
TestList6.append(dict({1:1}))

TestSet: set[int] = set(set({1,2}))
TestList3: list[int] = list(TestSet)

TestList4: list[dict[Hashable, AnyTFWR]]

TestAny1: AnyTFWR = dict(TestDict)
TestAny2: AnyTFWR = set(TestDict)
TestAny3: AnyTFWR = set(TestList)

append(TestList6, {2:2})