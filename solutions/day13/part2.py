from solutions.common import read_input
from .utils import parse_input, solve_all


def solve_part2(content):
    """Find total minimum tokens needed with translated coordinates."""
    return solve_all(parse_input(content), translate=True)


def main():
    DAY_NUMBER = 13
    content = read_input(DAY_NUMBER)
    result = solve_part2(content)
    return result


if __name__ == "__main__":
    main()
