from solutions.common import read_input
from .utils import parse_input, count_unique_paths


def solve_part2(content: str) -> int:
    """Find sum of ratings for all trailheads.

    Rating is the number of distinct hiking trails
    that begin at each trailhead.
    """
    grid, trailheads = parse_input(content)

    # Sum up number of unique paths from each trailhead
    return sum(count_unique_paths(start, grid) for start in trailheads)


def main():
    DAY_NUMBER = 10
    content = read_input(DAY_NUMBER)
    result = solve_part2(content)
    return result


if __name__ == "__main__":
    main()
