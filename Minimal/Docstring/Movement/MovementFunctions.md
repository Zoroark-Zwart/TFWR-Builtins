# move

Moves the drone into the specified `direction` by one tile.
If the drone moves over the edge of the farm it wraps back to the other side of the farm.

- `East ` = right
- `West ` = left
- `North` = up
- `South` = down

returns `True` if the drone has moved, `False` otherwise.

takes `200` ticks to execute if the drone has moved, `1` tick otherwise.

example usage:

```
move(North)
```

# can_move

Checks if the drone can move in the specified `direction`.

returns `True` if the drone can move, `False` otherwise.

takes `1` tick to execute.

example usage:

```
if can_move(North):
    move(North)
```

# get_pos_x

Gets the current x position of the drone.
The x position starts at `0` in the `West` and increases in the `East` direction.

returns a number representing the current x coordinate of the drone.

takes `1` tick to execute.

example usage:

```
x, y = get_pos_x(), get_pos_y()
```

# get_pos_y

Gets the current y position of the drone.
The y position starts at `0` in the `South` and increases in the `North` direction.

returns a number representing the current y coordinate of the drone.

takes `1` tick to execute.

example usage:

```
x, y = get_pos_x(), get_pos_y()
```

# get_world_size

Get the current size of the farm.

returns the side length of the grid in the north to south direction.

takes `1` tick to execute.

example usage:

```
for i in range(get_world_size()):
    move(North)
```
