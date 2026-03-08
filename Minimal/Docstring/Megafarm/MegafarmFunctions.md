# spawn_drone

Spawns a new drone in the same position as the drone that ran `spawn_drone(task)`. The new drone then begins executing the specified `task` function. After it is done, it will disappear automatically.

returns the a `Drone` object for the new drone or `None` if all drones are already spawned.

takes `200` ticks to execute if a drone was spawned, `1` otherwise.

example:

```
def harvest_column():
	for _ in range(get_world_size()):
		harvest()
		move(North)

while True:
	if spawn_drone(harvest_column):
		move(East)
```

# wait_for

Waits until the given `drone` terminates.

returns the return value of the function that the `drone` was running.

takes `1 + remaining task ticks` remaining in the given drone's task function.
takes `1` tick to execute if the awaited `drone` is already done.

example:

```
def get_entity_type_in_direction(dir):
	move(dir)
	return get_entity_type()

def zero_arg_wrapper():
	return get_entity_type_in_direction(North)
handle = spawn_drone(zero_arg_wrapper)
print(wait_for(handle))
```

# has_finished

Checks if the given 1drone1 has finished.

returns `True` if the drone has finished, `False` otherwise.

takes `1` tick to execute.

example:

```
drone = spawn_drone(function)
while not has_finished(drone):
	do_something_else()
result = wait_for(drone)
```

# max_drones

Gets the maximum number of drones available on the farm.

returns the maximum number of drones that you can have in the farm.

takes `1` tick to execute.

example:

```
while num_drones() < max_drones():
	spawn_drone("some_file_name")
	move(East)
```

# num_drones

Gets the current number of drones running a task on the farm.

returns the number of drones currently in the farm.

takes `1` tick to execute.

example:

```
while num_drones() < max_drones():
	spawn_drone("some_file_name")
	move(East)
```
