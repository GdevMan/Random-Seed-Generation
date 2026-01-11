# Random-Seed-Generation

A simple Python procedural world generator using random seeds.

## How it works

- Uses Python’s `random` module to create random worlds.  
- Accepts an optional seed to control the random number generator for reproducible worlds.  
- Uses an `options` array to represent terrain: `1` = land, `0` = water.  
- Has a `max_mem_usage` variable to limit the size of the rolling options list, keeping memory usage low for large worlds.
## For Game Use

You can easily integrate this generator into your own game or simulation:

1. **Import the functions** into your game script:
```from generate_world import generate, debug```

Generate a world (with optional seed for reproducibility):
```world, options = generate(size=200, max_mem_usage=102, seed=1234)```

Use the world data however you like:
  1 = land, 0 = water
  Example: iterate over world to create tiles, spawn objects, or render a map.

  Optional: Debug or visualize it:
  ```debug(world, options)```
