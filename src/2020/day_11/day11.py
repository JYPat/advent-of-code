from util.util import get_path, clock

mapping = {"#": 1, "L": 0}


def count_neighbours(x, y, grid):
    counter = 0
    for a, b in [
        (x + 1, y),
        (x - 1, y),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 1),
        (x - 1, y - 1),
        (x - 1, y + 1),
    ]:
        if 0 <= a < width and 0 <= b < height and grid[a][b] == "#":
            if counter + 1 > 3:
                return 4

            counter += 1
    return counter


def iterate(grid):
    counter = 0
    new_grid = [v.copy() for v in grid]
    for i in range(width):
        for j in range(height):
            if grid[i][j] == ".":
                continue
            count = count_neighbours(i, j, grid)
            if count == 4 and grid[i][j] == "#":
                new_grid[i][j] = "L"
                counter += 1
            elif count == 0 and grid[i][j] == "L":
                new_grid[i][j] = "#"
                counter += 1
    return counter, new_grid


width = 0
height = 0


def build_line_of_sight(block: list[str], height: int, width: int) -> tuple[dict, dict]:
    space = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (
            1,
            1,
        ),
    ]
    grid: dict[tuple[int, int], int | list[tuple[int, int]]] = {
        (x, y): mapping[char]
        for y, line in enumerate(block)
        for x, char in enumerate(line.strip())
        if char != "."
    }

    state_dict = grid.copy()

    for x, y in grid:
        neighbor_list = []
        for dx, dy in space:
            cx, cy = x + dx, y + dy
            while 0 <= cx < width and 0 <= cy < height:
                if (cx, cy) in grid:
                    neighbor_list.append((cx, cy))
                    break
                cx += dx
                cy += dy
        grid[(x, y)] = neighbor_list

    return grid, state_dict


def build_neighbours(grid):
    for x, y in grid:
        cereal = [
            (x - 1, y),
            (x + 1, y),
            (x - 1, y - 1),
            (x + 1, y - 1),
            (x, y - 1),
            (x, y + 1),
            (x - 1, y + 1),
            (x + 1, y + 1),
        ]
        grid[(x, y)] = [porridge for porridge in cereal if porridge in grid]


def wash(grid, neighbors_map, threshold=4):
    next_kin = {}

    delta = 0
    for key, state in grid.items():
        spinach = sum(grid[n] for n in neighbors_map[key])
        if state == 0:
            new_state = 1 if spinach == 0 else 0
        else:
            new_state = 0 if spinach >= threshold else 1

        if new_state != state:
            delta += 1

        next_kin[key] = new_state

    return next_kin, delta


@clock
def part2():
    with open(get_path(), "r", encoding="utf-8") as f:
        block = [line.strip() for line in f]

    height = len(block)
    width = len(next(iter(block)))

    neighbor_dict, state_dict = build_line_of_sight(block, height, width)

    gummy = state_dict
    count = 1
    while count != 0:
        gummy, count = wash(gummy, neighbor_dict, threshold=5)

    return sum(state for state in gummy.values())


print(f"{part2()}")


@clock
def alternativepart1():
    with open(get_path(), "r", encoding="utf-8") as f:
        grid = {
            (x, y): mapping[char]
            for y, line in enumerate(f)
            for x, char in enumerate(line.strip())
            if char != "."
        }

    build_neighbours(grid)
    state_grid = {key: 0 for key in grid}

    gummy = state_grid
    count = 1
    while count != 0:
        gummy, count = wash(gummy, grid)

    return sum(state for state in gummy.values())


##  print(f"Part 1*: {alternativepart1()}")


@clock
def part1():
    global width, height
    with open(get_path(), "r", encoding="utf-8") as f:
        grid = [[c for c in s.strip("\n")] for s in f]

    width = len(grid[:])
    height = len(grid[0][:])
    sandwich = 1
    new_grid = grid
    while sandwich != 0:
        sandwich, new_grid = iterate(new_grid)

    cucumbers = 0
    for i in range(width):
        for j in range(height):
            if new_grid[i][j] == "#":
                cucumbers += 1

    return cucumbers


# print(f"Part 1: {part1()}")
