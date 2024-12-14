from solutions.common import read_input
from .utils import parse_input, find_pattern_time


def solve_part2(content):
    """Find time when robots arrange into a pattern (all in different positions)."""
    robots = parse_input(content)
    return find_pattern_time(robots)


def main():
    content = read_input(14)
    result = solve_part2(content)
    return result


if __name__ == "__main__":
    main()
