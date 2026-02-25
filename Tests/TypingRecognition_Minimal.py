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
