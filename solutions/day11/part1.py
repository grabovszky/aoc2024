from solutions.common import read_input
from .utils import parse_input, simulate_blinks


def solve_part1(content):
    """Solve part 1: Count stones after 25 blinks."""
    stones = parse_input(content)
    return simulate_blinks(stones, 25)


def main():
    DAY_NUMBER = 11
    content = read_input(DAY_NUMBER)
    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
