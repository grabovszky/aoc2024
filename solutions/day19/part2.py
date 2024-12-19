from solutions.common import read_input
from .utils import parse_input, num_arrangements


def solve_part2(content):
    """Calculate total number of possible arrangements for all designs."""
    towels, designs = parse_input(content)
    # Convert towels to tuple for caching
    towels_tuple = tuple(towels)

    return sum(num_arrangements(design, towels_tuple) for design in designs)


def main():
    DAY_NUMBER = 19
    content = read_input(DAY_NUMBER)
    result = solve_part2(content)
    return result


if __name__ == "__main__":
    main()
