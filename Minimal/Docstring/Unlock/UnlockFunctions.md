# get_cost

Gets the cost of a `thing`

If `thing` is an entity: get the cost of planting it.
If `thing` is an unlock: get the cost of unlocking it at the specified level.

- returns a dictionary with items as keys and numbers as values. Each item is mapped to how much of it is needed.
- returns `None` for unlocks that are already unlocked (when no level specified).
- The optional `level` parameter specifies the upgrade level for unlocks.

takes `1` tick to execute.

example usage:

```
cost = get_cost(Unlocks.Carrots)
for item in cost:
    if num_items(item) < cost[item]:
        print('not enough items to unlock carrots')
```

# unlock

Has exactly the same effect as clicking the button corresponding to `unlock` in the research tree.

returns `True` if the unlock was successful, `False` otherwise.

takes `200` ticks to execute if it succeeded, `1` tick otherwise.

example usage:

```
unlock(Unlocks.Carrots)
```

# num_unlocked

Used to check if an unlock, entity, ground, item or hat is already unlocked.

returns `1` plus the number of times `thing` has been upgraded if `thing` is upgradable. Otherwise returns `1` if `thing` is unlocked, `0` otherwise.

takes `1` tick to execute.

example usage:

```
if num_unlocked(Unlocks.Carrots) > 0:
    plant(Entities.Carrot)
else:
    print("Carrots not unlocked yet")
```
