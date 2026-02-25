from Release.__builtins__minimal import *

from typing import overload

range(3)
range(1, 3)
range(1, 5, 2)

for i in range(1, 3):
    print(i)

for i in range(1, 5, 2):
    print(i)

def SpawnTester() -> None:
    return None

spawn_drone(SpawnTester)
spawn_drone("Test")
spawn_drone(2)
spawn_drone()
