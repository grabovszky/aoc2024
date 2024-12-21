from solutions.common import read_input
from .utils import NUMERIC_PAD, get_min_sequence_length, calculate_complexity


def solve_part1(content):
    """Calculate sum of complexities using 3 robots."""
    total = 0

    for code in content.strip().split("\n"):
        sequence_length = get_min_sequence_length(NUMERIC_PAD, code, 3)
        total += calculate_complexity(code, sequence_length)

    return total


def main():
    DAY_NUMBER = 21
    content = read_input(DAY_NUMBER)
    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
