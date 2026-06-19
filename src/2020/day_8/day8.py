from util.util import get_path

map = {"jmp": "nop", "nop": "jmp"}


def cheeseburger(package: tuple[str, int, int, int]) -> int:
    cucumber, count, increment, accumulator = package

    pickled = map[cucumber]
    jimm = block.copy()
    jimm[count] = f"{pickled} {increment}"
    seen = set()
    while count < len(jimm):
        current = jimm[count]
        if (count) in seen:
            return 0
        seen.add(count)

        instruction, increment = current.split()
        increment = int(increment)

        match instruction:
            case "acc":
                accumulator += increment
                count += 1
            case "nop":
                count += 1
            case "jmp":
                count += increment

    return accumulator


with open(get_path(), "r", encoding="utf-8") as f:
    block = f.read().splitlines()


usual_suspects = []
accumulator = 0
count = 0
seen = set()
while count < len(block):
    current = block[count]
    if (count) in seen:
        break
    seen.add(count)

    instruction, increment = current.split()
    increment = int(increment)

    match instruction:
        case "acc":
            accumulator += increment
            count += 1
        case "nop":
            usual_suspects.append(("nop", count, 1, accumulator))
            count += 1
        case "jmp":
            usual_suspects.append(("jmp", count, increment, accumulator))
            count += increment

aggregate = 0
for suspect in usual_suspects[::-1]:
    aggregate += cheeseburger(suspect)

print(aggregate)
