# get_entity_type

Find out what kind of entity is under the drone.

returns `None` if the tile is empty, otherwise returns the type of the entity under the drone.

takes `1` tick to execute.

example usage:

```
if get_entity_type() == Entities.Grass:
    harvest()
```

# get_ground_type

Find out what kind of ground is under the drone.

returns the type of the ground under the drone.

takes `1` tick to execute.

example usage:

```
if get_ground_type() != Grounds.Soil:
    till()
```

# get_water

Get the current water level under the drone.

returns the water level under the drone as a number between `0` and `1`.

takes `1` tick to execute.

example usage:

```
if get_water() < 0.5:
    use_item(Items.Water)
```

# num_items

Find out how much of `item` you currently have.

returns the number of `item` currently in your inventory.

takes `1` tick to execute.

example usage:

```
if num_items(Items.Fertilizer) > 0:
    use_item(Items.Fertilizer)
```

# get_companion

Get the companion preference of the plant under the drone.

returns a tuple of the form `(companion_type, (companion_x_position, companion_y_position))` or `None` if there is no companion.

takes `1` tick to execute.

example usage:

```
companion = get_companion()
if companion != None:
    plant_type, (x, y) = companion
    print("Companion:", plant_type, "at", x, ",", y)
```

# measure

Can measure some values on some entities. The effect of this depends on the entity.
Will work anynore inside of a maze and only on a `Entities.Apple`

overloads:
`measure()`: measures the entity under the drone.
`measure(direction)`: measures the neighboring entity in the `direction` of the drone.

Sunflower: returns the number of petals.
Maze: returns the position of the current treasure from anywhere in the maze.
Cactus: returns the size.
Dinosaur: returns the number corresponding to the type.
All other entities: returns `None`.

takes `1` tick to execute.

example usage:

```
num_petals = measure()
treasure_pos = measure()
```
