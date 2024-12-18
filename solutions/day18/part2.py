from solutions.common import read_input
from .utils import parse_input, find_shortest_path


def find_blocking_byte(bytes, size_space):
    """Find the byte that blocks the path using binary search."""
    lo, hi = 0, len(bytes)

    while lo < hi:
        mid = (lo + hi) // 2
        corrupted = set(bytes[:mid])

        # Check if path is blocked
        if find_shortest_path(corrupted, size_space) == size_space * size_space + 1:
            hi = mid - 1
        else:
            lo = mid + 1

    # Return coordinates of blocking byte
    y, x = bytes[mid]
    return f"{x},{y}"


def solve_part2(content, test_mode=False):
    """Find coordinates of byte that blocks the path."""
    bytes, size_space = parse_input(content, test_mode)
    return find_blocking_byte(bytes, size_space)


def main():
    return solve_part2(read_input(18))


if __name__ == "__main__":
    main()
