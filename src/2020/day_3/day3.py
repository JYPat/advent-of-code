from src.util.util import get_path

path = get_path()

lines = [line for line in open(path, "r", encoding="utf-8")]


def solution(skip: int, hops) -> int:
    hops = iter(hops)
    first_line = next(hops)
    width = len(first_line) - 1
    index = 0
    trees = 0

    for line in hops:
        index = (index + skip) % width

        if line[index] == "#":
            trees += 1

    return trees


def solution_two():
    inputs = [1, 3, 5, 7]
    product = 1
    for input in inputs:
        product *= solution(input, lines)

    separate = (
        x for i, x in enumerate(open(path, "r", encoding="utf-8")) if i % 2 == 0
    )
    product *= solution(1, separate)

    print(product)


solution_two()
