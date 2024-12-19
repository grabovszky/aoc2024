from solutions.common import read_input
from .utils import parse_input, solve_designs_parallel


def solve_part2(content):
    """Calculate total number of possible arrangements for all designs."""
    towels, designs = parse_input(content)

    # Process all designs in parallel
    results = solve_designs_parallel(designs, towels)
    return sum(results)


def main():
    DAY_NUMBER = 19
    content = read_input(DAY_NUMBER)
    result = solve_part2(content)
    return result


if __name__ == "__main__":
    main()
