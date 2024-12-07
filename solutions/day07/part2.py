from .utils import parse_input, solve
from solutions.common import read_input


def solve_part2(content):
    equations = parse_input(content)
    return solve(equations, allow_concat=True)


def main():
    DAY_NUMBER = 7
    content = read_input(DAY_NUMBER)
    result = solve_part2(content)
    return result


if __name__ == "__main__":
    main()
