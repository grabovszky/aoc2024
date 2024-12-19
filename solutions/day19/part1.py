from solutions.common import read_input
from .utils import parse_input, num_arrangements


def solve_part1(content):
    """Calculate how many designs are possible with given towel patterns."""
    towels, designs = parse_input(content)
    # Convert towels to tuple for caching
    towels_tuple = tuple(towels)

    return sum(num_arrangements(design, towels_tuple) > 0 for design in designs)


def main():
    DAY_NUMBER = 19
    content = read_input(DAY_NUMBER)
    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
