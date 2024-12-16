from solutions.common import read_input
from .utils import parse_input, find_paths


def solve_part1(content):
    """Find lowest possible score through maze."""
    grid, start, end = parse_input(content)
    dist, _ = find_paths(grid, start, end)
    return min(dist[(*end, h)] for h in "LRUD")


def main():
    return solve_part1(read_input(16))


if __name__ == "__main__":
    main()
