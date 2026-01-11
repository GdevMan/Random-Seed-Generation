import random
def generate(size, max_mem_usage, seed=None):
    if seed == None:
        seed = random.randint(1, 10000)
    random.seed(seed)
    options = [1, 0]
    map = []
    for i in range(size):
        choice = random.choice(options)
        map.append(choice)
        if choice == 1:
            options.append(1)
        else:
            options.append(0)
        if len(options) > max_mem_usage:
            options.pop(0)
    return map, options

def debug(world, options):
    print('--- MAP ---')
    print(*world)
    print('--- MAP GENERATION DATA ---')
    print(*options)
    print('--- MAP GENERATION DATA LENGTH ---')
    print(len(options))
if __name__ == '__main__':
    world1, options1 = generate(100, 102, 1375)
    debug(world1, options1)

    world2, options2 = generate(100, 102, 1375)
    debug(world2, options2)