from solutions.common import read_input
from .utils import NUMERIC_PAD, get_min_sequence_length, calculate_complexity


def solve_part2(content):
    """Calculate sum of complexities using 26 robots."""
    total = 0

    for code in content.strip().split("\n"):
        sequence_length = get_min_sequence_length(NUMERIC_PAD, code, 26)
        total += calculate_complexity(code, sequence_length)

    return total


def main():
    DAY_NUMBER = 21
    content = read_input(DAY_NUMBER)
    result = solve_part2(content)
    return result


if __name__ == "__main__":
    main()
