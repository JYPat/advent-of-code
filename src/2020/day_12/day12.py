from util.util import get_path, clock


def up(coords, increment):
    coords[1] += increment


def down(coords, increment):
    coords[1] -= increment


def left(coords, increment):
    coords[0] -= increment


def right(coords, increment):
    coords[0] += increment


def chdir(dir, increment):
    return (dir + (increment // 90)) % 4


def ell_one(coords):
    return sum(abs(v) for v in coords)


with open(get_path(), "r", encoding="utf-8") as f:
    block = f.read().splitlines()
dirs = ["N", "E", "S", "W"]
mapping_abs = {
    "N": up,
    "S": down,
    "E": right,
    "W": left,
}


def part_one():
    coordinates = [0, 0]
    dir = 1
    for line in block:
        char = line[0]
        increment = int(line[1:])

        if char not in mapping_abs:
            if char == "F":
                mapping_abs[dirs[dir]](coordinates, increment)
            elif char == "R":
                dir = chdir(dir, increment)
            elif char == "L":
                dir = chdir(dir, -increment)
            continue

        mapping_abs[char](coordinates, increment)

    print(f"Part 1: {ell_one(coordinates)}")


@clock
def part_two():
    ship_coordinates = [0, 0]
    waypoint_coordinates = [10, 1]

    def warp(ship_pos, waypoint_pos, scale):
        transform = [
            scale * (waypoint_pos[0]),
            scale * (waypoint_pos[1]),
        ]
        return [ship_pos[0] + transform[0], ship_pos[1] + transform[1]]

    def rotation(waypoint_pos, increment):
        steps = increment // 90
        if steps % 2 == 0:
            return [-1 * waypoint_pos[0], -1 * waypoint_pos[1]]

        sign = increment / increment
        if (steps - 1) % 4 == 0:
            sign *= -1
        flat_mat = [-1 * sign, 1 * sign]
        x = waypoint_pos[1] * flat_mat[1]
        y = waypoint_pos[0] * flat_mat[0]
        return [int(x), int(y)]

    for line in block:
        char = line[0]
        increment = int(line[1:])

        if char not in mapping_abs:
            match char:
                case "F":
                    ship_coordinates = warp(
                        ship_coordinates, waypoint_coordinates, increment
                    )
                case "L":
                    waypoint_coordinates = rotation(waypoint_coordinates, increment)
                case "R":
                    waypoint_coordinates = rotation(waypoint_coordinates, -increment)
            continue

        mapping_abs[char](waypoint_coordinates, increment)
    print(f"Part 2: {ell_one(ship_coordinates)}")


part_two()
