from solutions.common import read_input
from .utils import parse_input, calculate_properties


def solve_part1(content):
    """Calculate total price of fencing all regions using perimeter."""
    grid = parse_input(content)
    return calculate_properties(grid, count_corners=False)


def main():
    DAY_NUMBER = 12
    content = read_input(DAY_NUMBER)
    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
