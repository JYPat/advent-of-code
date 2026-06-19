from util.util import get_path

with open(get_path(), "r", encoding="utf-8") as f:
    block = f.read().splitlines()

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
            count += 1
        case "jmp":
            count += increment

print(accumulator)
