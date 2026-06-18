from src.util.util import get_path
import re

with open(get_path(), "r", encoding="utf-8") as f:
    block = f.read().split("\n\n")


def part1(block: list[str]):
    count = 0
    for group in block:
        valid = set(re.findall(r"[a-z]", group))
        count += len(valid)


# print(count)


def part2(block: list[str]):
    count = 0
    for group in block:
        friends = group.rsplit("\n")
        smart_friends = [set(friend) for friend in friends if friend]
        count += len(set.intersection(*smart_friends))

    return count


print(f"Part 2: {part2(block)}")
