# spawn_drone

Spawns a new drone in the same position as the drone that ran `spawn_drone(task, *args)`. The new drone then begins executing the provided `task` function. The rest of the arguments are copied and passed into the specified `task` function. After it is done, it will disappear automatically.

`*P` - list of parameters that your task can can take as arguments. Must match the type of arguments you give to `spawn_drone` with the parameter types you assign of the `task` that you provide.
`R` - the return type of your drone. Must must the return type of of the `task` you provide.

Passes the `*args` to the provided `task` when that drone runs.

returns a `Drone[R]` object for the new drone or `None` if all drones are already spawned.
Note: `None` is not type hinted to reduce complexity when using variables with functions that accept a `Drone`.

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
`R` - the return type of your drone. Must must the return type of of the `task` you provided with `spawn_drone`.

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

Checks if the given `drone` has finished.

`R` - the return type of your drone. Must must the return type of of the `task` you provided with `spawn_drone`.

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
