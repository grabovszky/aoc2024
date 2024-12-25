from solutions.common import read_input
from .utils import parse_input, count_fitting_pairs


def solve_part1(content):
    """Find number of lock/key pairs that fit together."""
    locks, keys = parse_input(content)
    return count_fitting_pairs(locks, keys)


def main():
    return solve_part1(read_input(25))


if __name__ == "__main__":
    main()
