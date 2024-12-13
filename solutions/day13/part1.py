from solutions.common import read_input
from .utils import parse_input, solve_all


def solve_part1(content):
    """Find total minimum tokens needed to win all possible prizes."""
    return solve_all(parse_input(content))


def main():
    DAY_NUMBER = 13
    content = read_input(DAY_NUMBER)
    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
