from solutions.common import read_input
from .utils import parse_input, find_shortest_path


def solve_part1(content, test_mode=False):
    """Find shortest path after first 1024 bytes have fallen."""
    bytes, size_space = parse_input(content, test_mode)

    # For test input, use only first 12 bytes
    num_bytes = 12 if test_mode else 1024
    corrupted = set(bytes[:num_bytes])

    return find_shortest_path(corrupted, size_space)


def main():
    return solve_part1(read_input(18))


if __name__ == "__main__":
    main()
