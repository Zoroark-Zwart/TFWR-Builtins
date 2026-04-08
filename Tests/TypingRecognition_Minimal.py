from Release.__builtins__minimal import *

range(3) # Correct usage
range(3.5) # Correct usage
range("3") # Should error and say not assignable
range(1, 3) # Correct usage
range(1.1, 3.5) # Correct usage
range("1", "3") # Should error and say not assignable
range(1, 5, 2) # Correct usage
range(1.1, 5.6, 2.01) # Correct usage
range("1", "5", "2") # Should error and say not assignable
range() # Should error and say no arguments given

# Correct usage
# Should assign int to i
# Return the range Python class
for i in range(3):
    print(i)

# Correct usage
# Should assign int to i
# Return the range Python class
for i in range(1, 3):
    print(i)

# Correct usage
# Should assign int to i
# Return the range Python class
for i in range(1, 5, 2):
    print(i)


# Spawn Drone
def SpawnTester():
    ...

spawn_drone(SpawnTester) # Correct usage
spawn_drone("Test") # Should error and say not assignable
spawn_drone(2) # Should error and say not assignable
spawn_drone() # Should error and say no arguments given


TestDict = dict()
TestList = list()
TestSet = set()

dict.len(TestList) # Error
dict.len(TestDict) # Proper usage
pop(dict({"1":1}), 1)



TestListInt : list[int] = list()
TestListInt.append(1)
list(TestListInt)

list(1) # Error - wrong type
list(1, 2) # Error - positional
TestList.append(8)
TestDict.len()
TestSet.add(1)

TestList2 = []
TestList2.len() # Can this be done? Overwrite lists that use [] and add methods?


TestDict2 = dict({1:1,2:2,3:3})
TestDict2.pop(1)

pop(TestDict2, 1)

append(list([1]), 2)
append([1], 2)

list({1})
list(list([1]))

# from builtins import (bool as _bool, int as _int, float as _float, str as string,
# 					  range as range_class,
# 					  tuple as _tuple, list as _list, set as _set, dict as _dict)

from typing import Sequence

class CustomList[Any](_list[Any]):
	def __setitem__(self, key, value):
		return super().__setitem__(key, value)
	def __iadd__(self, value):
		return super().__iadd__(value)
	def __add__(self, value):
		return super().__add__(value)



TesterAny: Any = 1
TesterCustomList: CustomList[int] = CustomList()
TesterCustomList = [1] # Don't think this is possible to address?


TesterList: list[Any] = list()
TesterList = [1] # Don't think this is possible to address?

def HelloDrone():
    ...

def HelloDroneArgument(hello):
    ...

DroneHandle: Drone = spawn_drone(HelloDrone) # Proper usage
DroneHandle: Drone = spawn_drone(HelloDroneArgument) # Wrong type error due to function paramters
has_finished(DroneHandle) # Proper usage
has_finished(1) # Wront type error
wait_for(DroneHandle) # Proper usage
wait_for("a") # Wront type error


simulate("Hi", {Unlocks.Cactus: 1}, {Items.Power: 1000}, {}, 1, 250)

UnlockDict = dict()
UnlockDict[Unlocks.Cactus] = 1

ItemDict = dict()
ItemDict[Items.Power] = 1000

simulate("Hi", UnlockDict, ItemDict, {}, 1, 250)

MyList: list[int] = list([1])

ListAny : list[Any] = [1, "hhih", 1.1]

remove(MyList, 1)
insert(MyList, 1, 1)

MySet : set[int] = {1, 2, 3}

remove(MySet, 1)

print(list([1]))
print(((1, 2), (3, 3)))
print(({1, 2}, (3, 3)))
print({(1, 2), (3, 4)})

TestString : string = str(1)

class Custom():
      ...

TestSetCustom : set[Custom]

simulate()

Literal[1]

TestAny : Any = ((1, 2, 3), 1, 2.3, "string", ((1, 2), (3, "Hey")), True, False)
TestAny1 : Any = 1
Test1Hashable : Hashable = 1
TestAnyHashable : Hashable = (((0, 1), 2, 3), (1, 2, 3))
TestDictHashable : dict[Hashable, Any] = {(1, 2, 3): 1}

Primitive
Enums
Hashable
Any
AnyIterable


TestDictAnyHuge : dict[Hashable, Any] = {1: [1, 2, 3, (1, 2, 3), False, None, {1, 2, 3}]}
TestDictSmall : dict[Hashable, Any] = {1: 1}

Entities.Apple
for entity in Entities:
	print(entity)
