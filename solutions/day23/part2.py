from solutions.common import read_input
from .utils import parse_input, find_max_clique


def solve_part2(content):
    """Find largest fully-connected group of computers."""
    neighbors = parse_input(content)
    max_clique = find_max_clique(neighbors)
    return ",".join(sorted(max_clique))


def main():
    return solve_part2(read_input(23))


if __name__ == "__main__":
    main()
