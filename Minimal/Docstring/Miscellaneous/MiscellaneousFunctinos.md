# do_a_flip

Makes the drone do a flip! This action is not affected by speed upgrades.

returns `None`

takes 1s to execute.

example usage:

```
while True:
	do_a_flip()
```

# pet_the_piggy

Pets the piggy! This action is not affected by speed upgrades.

returns `None`

takes 1s to execute.

example usage:

```
while True:
	pet_the_piggy()
```

# leaderboard_run

Starts a timed run for the `leaderboard` using the specified `file_name` as a starting point.
`speedup` sets the starting speedup.

returns `None`

takes `200` ticks to execute.

example usage:

```
leaderboard_run(Leaderboards.Fastest_Reset, "full_run", 256)
```
