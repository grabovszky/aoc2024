from solutions.common import read_input
from .utils import parse_input, solve


def solve_part1(content):
    equations = parse_input(content)
    return solve(equations, allow_concat=False)


def main():
    DAY_NUMBER = 7
    content = read_input(DAY_NUMBER)
    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
