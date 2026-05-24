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


pop([1, 2])
pop([1, 2], 1)

min([1, 2], [3, 4], list([1, 2]), ['s', 'd'])
min([1, 2], [3, 4], list([1, 2]))

def DroneFunction() -> float | list[int]:
    TestNum = random()

    if TestNum:
        return 1.3
    else:
        return list([1, 2])

MyDrone: Drone[float | list[int]] | None = spawn_drone(DroneFunction)

plant(entity = Entities.Bush)
plant(Entities.Carrot, entity = Entities.Bush)

min([1, "Hel"])
max(1, "Hello")

min([1, 1])
max(1, 2, 3.3)
min(range(10))

TestMeasure: Measure = measure(North)

@overload
def Test(a:int) -> int: ...
@overload
def Test(a:float) -> float: ...

def Test(a:int|float) -> int | float:
    """
    hjsjdhsjhd
    """
    ...


TestCost: Cost = get_cost(Entities.Bush)