# get_time

Get the current game time.

returns the time in seconds since the start of the game.

takes `0` tick to execute.

example usage:

```
start = get_time()
do_something()
time_passed = get_time() - start
```

# get_tick_count

Used to measure the number of ticks performed.

returns the number of ticks performed since the start of execution.

takes `0` tick to execute.

example usage:

```
do_something()
print(get_tick_count())
```

# set_execution_speed

Limits the speed at which the program is executed to better see what's happening.

- A `speed` of `1` is the speed the drone has without any speed upgrades.
- A `speed` of `10` makes the code execute `10` times faster and corresponds to the speed of the drone after `9` speed upgrades.
- A `speed` of `0.5` makes the code execute at half of the speed without speed upgrades. This can be useful to see what the code is doing.

If `speed` is faster than the execution can currently go it will just go at max speed.

If `speed` is `0` or negative, the speed is changed back to max speed.
The effect will also stop when the execution stops.

returns `None`

takes `200` ticks to execute.

example usage:

```
set_execution_speed(1)
```

# set_world_size

Limits the size of the farm to better see what's happening.
Also clears the farm and resets the drone position.

- Sets the farm to a `size` x `size` grid.
- The smallest `size` possible is `3`.
- A `size` smaller than `3` will change the grid back to its full size.
- The effect will also stop when the execution stops.

returns `None`

takes `200` ticks to execute.

example usage:

```
set_world_size(5)
```

# simulate

Starts a simulation for the leaderboard using the specified `file_name` as a starting point.

`sim_unlocks`: A sequence containing the starting unlocks. These unlocks can be one of these:

- `dict[Unlock, int]` - Example: `{Unlocks.Expand: 2, Unlocks.Cactus: 1}`
- `tuple[tuple[Unlock, int]]` - Example: `((Unlocks.Expand, 2), (Unlocks.Cactus, 1))`
- `list[tuple[Unlock, int]]` - Example: `[(Unlocks.Expand, 2), (Unlocks.Cactus, 1)]`
- `tuple[Unlock]` - Captures your current unlock level of specific unlocks from your main farm. Example: `(Unlocks.Expand, Unlocks.Cactus)`
- `list[Unlock]` - Captures your current unlock level of specific unlocks from your main farm. Example: `[Unlocks.Expand, Unlocks.Cactus]`
- `Unlocks` - Captures all of your current unlock levels from your main farm.

`sim_items`: A dict mapping items to amounts. The simulation starts with these items.

`sim_globals`: A dict mapping variable names to values. The simulation starts with these variables in the global scope. Make sure any variables assigned in here are not assigned in the simulation code as that will override the vales from this dict.

`seed`: The random seed of the simulation. Must be a positive integer.

`speedup`: The starting speedup. The simulation may not reach the stated `speedup` value if it cannot properly speedup computation. Common causes for this include use of multiple drones or eating up too many ticks in a loop per iteration (for example a wait loop using pass).

returns the time it took to run the simulation.

takes `200` ticks to execute.

example usage:

```
filename = "f1"
sim_unlocks = Unlocks
sim_items = {Items.Carrot : 10000, Items.Hay : 50}
sim_globals = {"a" : 13}
seed = 0
speedup = 64
run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
```
