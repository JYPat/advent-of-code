import enum

from util.util import get_path, clock


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


print(f"Part 1: {part1()}")
