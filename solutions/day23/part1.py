from solutions.common import read_input
from .utils import parse_input, find_triplets, has_t_computer


def solve_part1(content):
    """Count triplets containing at least one 't' computer."""
    neighbors = parse_input(content)
    triplets = find_triplets(neighbors)
    return sum(1 for triplet in triplets if has_t_computer(triplet))


def main():
    return solve_part1(read_input(23))


if __name__ == "__main__":
    main()
