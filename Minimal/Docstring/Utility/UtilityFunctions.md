# print

Prints `something` into the air above the drone using smoke. This action is not affected by speed upgrades.
Multiple values can be printed at once.

returns `None`

takes 1s to execute.

example usage:

```
print('ground:', get_ground_type())
```

# quick_print

Prints a value just like `print()` but it doesn't stop to write it into the air so it can only be found on the output page.

returns `None`

takes `0` ticks to execute.

example usage:

```
quick_print('hi mom')
```
