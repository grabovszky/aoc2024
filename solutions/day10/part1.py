from solutions.common import read_input
from .utils import parse_input, find_reachable_peaks


def solve_part1(content: str) -> int:
    """Find sum of scores for all trailheads.

    Score is the number of height-9 positions reachable
    from each trailhead.
    """
    grid, trailheads = parse_input(content)

    # Sum up number of reachable peaks from each trailhead
    return sum(len(find_reachable_peaks(start, grid)) for start in trailheads)


def main():
    DAY_NUMBER = 10
    content = read_input(DAY_NUMBER)
    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
