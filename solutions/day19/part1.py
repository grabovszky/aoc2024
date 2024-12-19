from solutions.common import read_input
from .utils import parse_input, solve_designs_parallel


def solve_part1(content):
    """Calculate how many designs are possible with given towel patterns."""
    towels, designs = parse_input(content)

    # Process all designs in parallel
    results = solve_designs_parallel(designs, towels)
    return sum(1 for result in results if result > 0)


def main():
    DAY_NUMBER = 19
    content = read_input(DAY_NUMBER)
    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
