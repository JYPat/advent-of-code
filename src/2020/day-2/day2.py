from collections import Counter
import sys

if len(sys.argv) < 2:
    print("USAGE: python script.py INPUT/DEMO")
    sys.exit(1)

file, field = sys.argv[0].strip(".py"), sys.argv[1]

if field == "INPUT":
    path = f"./input_{file}.txt"
elif field == "DEMO":
    path = f"./demo_{file}.txt"
else:
    print("Usage: python script.py INPUT/DEMO")
    sys.exit(1)

lines = (line for line in open(path, "r", encoding="utf-8"))


def solution():
    number_of_valids = 0

    for line in lines:
        domain, character, password = line.split()

        lower_limit, upper_limit = domain.split("-")
        character = character[0]
        password = Counter(password)

        if int(lower_limit) <= password[character] <= int(upper_limit):
            number_of_valids += 1

    print(number_of_valids)


def solution_two():
    number_of_valids = 0

    for line in lines:
        domain, character, password = line.split()

        lower_limit, upper_limit = domain.split("-")
        character = character[0]

        first_position, second_position = (
            password[int(lower_limit) - 1],
            password[int(upper_limit) - 1],
        )
        counter = Counter([first_position, second_position])

        if counter[character] == 1:
            number_of_valids += 1

    print(number_of_valids)


solution_two()
