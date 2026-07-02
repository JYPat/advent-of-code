from util.util import get_path

with open(get_path(), "r", encoding="utf-8") as f:
    block = f.read().splitlines()


def part_one():
    earliest_leave = int(block[0])
    schedule = block[1].split(",")
    ids = [int(id) for id in schedule if id.isdigit()]
    time_to = [(id - (earliest_leave % id)) for id in ids]
    best_index = time_to.index(min(time_to))

    print(f"Part 1: {(ids[best_index] * time_to[best_index])}")


def part_two():
    schedule = block[1].split(",")
    keys = {
        int(mod): (-i) % int(mod) for i, mod in enumerate(schedule) if mod.isdigit()
    }
    x, lcm = 0, 1
    for mod, constraint in keys.items():
        while x % mod != constraint:
            x += lcm
        lcm *= mod

    print(f"Part 2: {x}")


part_two()
