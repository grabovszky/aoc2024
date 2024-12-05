from solutions.common import read_input
from .utils import parse_input


def solve_part1(content):
    left_list, right_list = parse_input(content)

    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Calculate the total distance between the pairs
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    return total_distance


def main():
    DAY_NUMBER = 1
    content = read_input(DAY_NUMBER)

    # Solve Part 1
    result = solve_part1(content)
    print(f"Day {DAY_NUMBER}, Part 1 solution: {result}")


if __name__ == "__main__":
    main()
