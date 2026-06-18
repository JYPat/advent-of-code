from src.util.util import get_path

with open(get_path(), "r", encoding="utf-8") as f:
    block = [line.rstrip("\r\n") for line in f]


def part1(block: list[str]):
    highest = 0

    for row in block:
        row_number = 0
        seat_number = 0
        branch_length = 128
        twig_length = 8
        for node in row:
            if node in ["F", "B"]:
                branch_length //= 2
                row_number = max(
                    (
                        row_number - branch_length
                        if node == "F"
                        else row_number + branch_length
                    ),
                    row_number,
                )
            else:
                twig_length //= 2
                seat_number = max(
                    (
                        seat_number - branch_length
                        if node == "L"
                        else seat_number + twig_length
                    ),
                    seat_number,
                )

        product = (row_number * 8) + seat_number
        print(
            f"Row number: {row_number}, Seat number: {seat_number}, Product: {product}"
        )
        highest = product if product > highest else highest

    return highest


# print(f"{part1(block)}")
def part2(block: list[str]):
    seen = set()

    for row in block:
        row_number = 0
        seat_number = 0
        branch_length = 128
        twig_length = 8
        for node in row:
            if node in ["F", "B"]:
                branch_length //= 2
                row_number = max(
                    (
                        row_number - branch_length
                        if node == "F"
                        else row_number + branch_length
                    ),
                    row_number,
                )
            else:
                twig_length //= 2
                seat_number = max(
                    (
                        seat_number - branch_length
                        if node == "L"
                        else seat_number + twig_length
                    ),
                    seat_number,
                )

        product = (row_number * 8) + seat_number
        seen.add(product)

    our_seat = set(range(min(seen), max(seen))) - seen
    return our_seat


# print(f"Part 2: {part2(block)}")


def get_seat_id(line: str):
    row = int(line[:7].translate(str.maketrans("FB", "01")), 2)
    column = int(line[7:].translate(str.maketrans("LR", "01")), 2)

    return (row * 8) + column


def fastpart1(block: list[str]):
    return max(map(get_seat_id, block))


print(f"Part 1: {fastpart1(block)}")

# interesting
