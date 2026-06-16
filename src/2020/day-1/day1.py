import sys
import math

if len(sys.argv) < 2:
    print("Usage: python script.py INPUT/DEMO")
    sys.exit(1)

file, field = sys.argv[0].strip(".py"), sys.argv[1]

if field == "INPUT":
    path = f"./input_{file}.txt"
elif field == "DEMO":
    path = f"./demo_{file}.txt"
else:
    print("Usage: python script.py INPUT/DEMO")
    sys.exit(1)

lines = sorted([int(line) for line in open(path, "r", encoding="utf-8")])


def solution(target: int) -> tuple[int, int] | None:
    a, b = 0, len(lines) - 1

    for _ in range(len(lines)):
        sum = lines[a] + lines[b]
        if sum == target:
            return (lines[a], lines[b])
        elif sum > target:
            b -= 1
        elif sum < target:
            a += 1

    return None


def solution_two():
    lines = sorted([int(line) for line in open(path, "r", encoding="utf-8")])

    for line in lines:
        target = 2020 - line
        answer = solution(target)
        if answer:
            triplet = [line, *answer]
            print(f"{math.prod(triplet)}")


solution_two()
