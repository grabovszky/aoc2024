from solutions.common import read_input
from .utils import parse_input, count_quadrants


def solve_part1(content, width=101, height=103):
    """Calculate safety factor by counting robots in quadrants after 100 seconds."""
    robots = parse_input(content)
    return count_quadrants(robots, width, height)


def main():
    content = read_input(14)
    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
