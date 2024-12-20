from solutions.common import read_input
from .utils import parse_input, bfs, count_saving_cheats


def solve_part1(content):
    """Find number of cheats saving at least 100 picoseconds with jump size 2."""
    grid, start, end = parse_input(content)

    # Get distances from both start and end
    start_dists, base_dist = bfs(grid, start, end)
    end_dists, _ = bfs(grid, end, start)

    return count_saving_cheats(grid, start_dists, end_dists, base_dist, max_jump=2)


def main():
    DAY_NUMBER = 20
    content = read_input(DAY_NUMBER)
    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
