from Release.__builtins__minimal import *
#  from __builtins__ import *

def DroneFunction() -> string:
    ...

MyDrone : Drone[string] = spawn_drone(DroneFunction)

DroneReturn : string = wait_for(MyDrone)