from util.util import get_path, clock

with open(get_path(), "r", encoding="utf-8") as f:
    block = [int(v) for v in f]

PREAMBLE = 25


@clock
def part1(block: list[int], preamble: int):
    for i in range(preamble, len(block)):
        target = block[i]
        stage_range = block[i - preamble : i]

        seen = set()
        for number in stage_range:
            if (target - number) in seen:
                break
            seen.add(number)
        else:
            return target

    return 0


@clock
def part2(block: list[int], target: int):
    if target == 0:
        return

    a = 0
    current_sum = 0
    for b in range(len(block)):
        current_sum += block[b]

        while current_sum >= target and a <= b:
            if b - a >= 1 and current_sum == target:
                cucumbers = block[a : b + 1]
                return min(cucumbers) + max(cucumbers)

            current_sum -= block[a]
            a += 1

    return 0


target = part1(block, PREAMBLE)
print(target)
print(f"Part 2: {part2(block, target)}")
