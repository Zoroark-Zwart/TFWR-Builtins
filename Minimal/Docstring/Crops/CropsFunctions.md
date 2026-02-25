# harvest

Harvests the entity under the drone.
If you harvest an entity that can't be harvested, it will be destroyed.

returns `True` if an entity was removed, `False` otherwise.

takes `200` ticks to execute if an entity was removed, `1` tick otherwise.

example usage:

```
harvest()
```

# can_harvest

Used to find out if plants are fully grown.

returns `True` if there is an entity under the drone that is ready to be harvested, `False` otherwise.

takes `1` tick to execute.

example usage:

```
if can_harvest():
	harvest()
```

# plant

Spends the cost of the specified `entity` and plants it under the drone.
It fails if you can't afford the plant, the ground type is wrong or there's already a plant there.

returns `True` if it succeeded, `False` otherwise.

takes `200` ticks to execute if it succeeded, `1` tick otherwise.

example usage:

```
plant(Entities.Bush)
```

# swap

Swaps the entity under the drone with the entity next to the drone in the specified `direction`.

- Doesn't work on all entities.
- Also works if one (or both) of the entities are `None`.

returns `True` if it succeeded, `False` otherwise.

takes `200` ticks to execute on success, `1` tick otherwise.

example usage:

```
swap(North)
```

# till

Tills the ground under the drone into soil. If it's already soil it will change the ground back to grassland.

returns `None`

takes `200` ticks to execute.

example usage:

```
till()
```

# use_item

Attempts to use the specified `item` `n` times. Can only be used with some items including `Items.Water`, `Items.Fertilizer` and `Items.Weird_Substance`.

returns `True` if an item was used, `False` if the item can't be used or you don't have enough.

takes `200` ticks to execute if it succeeded, `1` tick otherwise.

example usage:

```
if use_item(Items.Fertilizer):
	print("Fertilizer used successfully")
```

# clear

Removes everything from the farm, moves the drone back to position `(0,0)` and changes the hat back to the default.

returns `None`

takes `200` ticks to execute.

example usage:

```
clear()
```

# change_hat

Changes the hat of the drone to the specified `hat`.

returns `None`

takes `200` ticks to execute.

example usage:

```
change_hat(Hats.Dinosaur_Hat)
```
