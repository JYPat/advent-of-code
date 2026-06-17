from src.util.util import get_path
import re

with open(get_path(), "r", encoding="utf-8") as f:
    lines = f.read().split("\n\n")

expected_field = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
}


def validate_height(input: str):
    if len(input) < 3:
        return False

    if input[-2:] not in ["cm", "in"]:
        return False

    try:
        height = int(input[:-2])
        if input[-2:] == "cm":
            return 150 <= height <= 193
        elif input[-2:] == "in":
            return 59 <= height <= 76

    except ValueError:
        return False

    return False


validators = {
    "byr": lambda value: value.isdigit() and 1920 <= int(value) <= 2002,
    "iyr": lambda value: value.isdigit() and 2010 <= int(value) <= 2020,
    "eyr": lambda value: value.isdigit() and 2020 <= int(value) <= 2030,
    "hgt": lambda height: validate_height(height),
    "hcl": lambda hair: bool(re.fullmatch(r"#[0-9a-f]{6}", hair)),
    "ecl": lambda color: color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda value: len(value) == 9 and value.isdigit,
    "cid": lambda ignore: True,
}


def part1(lines: list[str]) -> int:
    count = 0
    for line in lines:
        seen = set()
        key_value = line.split()
        seen = set([key.partition(":")[0] for key in key_value])

        print(seen)
        if (seen == expected_field) or (expected_field - seen) == {"cid"}:
            count += 1

    return count


# print(f"Part 1: {part1(lines)}")


def part2(lines: list[str]) -> int:
    count = 0

    for line in lines:
        two_tuples = [tuple(key.split(":")) for key in line.split()]
        seen = set(doublets[0] for doublets in two_tuples)

        if not ((seen == expected_field) or (expected_field - seen) == {"cid"}):
            continue

        print(two_tuples)
        parsed = dict(two_tuples)
        statement = all(validators[key](value) for key, value in parsed.items())

        if statement:
            count += 1

    return count


print(f"Part 2: {part2(lines)}")
