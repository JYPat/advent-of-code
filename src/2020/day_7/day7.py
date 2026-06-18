from collections import defaultdict

from src.util.util import get_path
import re


def part1(block):
    dictionary = dict()
    for line in block:
        key = line.split("bag", maxsplit=1)[0].strip()
        if any(char.isdigit() for char in line) and key != "shiny gold":
            values = re.findall(r"\d+ (.*?) bags?", line)
            for v in values:
                dictionary.setdefault(v, []).append(key)

    stack = ["shiny gold"]
    seen = set()
    while stack:
        current = stack.pop()
        consider = dictionary.get(current, [])
        seen.update(consider)

        if not consider:
            continue

        stack.extend(consider)

    return len(seen)


def part2(block):
    dictionary = dict()
    for line in block:
        if any(char.isdigit() for char in line):
            key = line.split("bag", maxsplit=1)[0].strip()
            values = re.findall(r"(\d+) (.*?) bags?", line)
            dictionary.setdefault(key, []).extend(values)

    total = defaultdict(int)
    stack = [("1", "shiny gold")]
    while stack:
        current_multiplier, current_bag = stack.pop()
        current_multiplier = int(current_multiplier)
        print(current_bag)
        print(current_multiplier)
        print()
        total[current_bag] += current_multiplier

        if current_bag in dictionary:
            for quantity, item in dictionary[current_bag]:
                total_quantity = int(quantity) * current_multiplier
                stack.append((str(total_quantity), item))

    total_purchases = sum(v for v in total.values())

    return total_purchases - 1  # for the shiny gold bag


with open(get_path(), "r", encoding="utf-8") as f:
    block = (line.rsplit("\n")[0] for line in f)

    # print(f"Part 1: {part1(block)}")
    print(f"Part 2: {part2(block)}")
