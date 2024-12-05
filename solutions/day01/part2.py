from solutions.common import read_input
from .utils import parse_input
from collections import Counter


def solve_part2(content):
    left_list, right_list = parse_input(content)

    # Count occurrences of each number in the right list
    right_counts = Counter(right_list)

    # Calculate the similarity score
    similarity_score = sum(num * right_counts.get(num, 0) for num in left_list)
    return similarity_score


def main():
    DAY_NUMBER = 1
    content = read_input(DAY_NUMBER)

    # Solve Part 2
    result = solve_part2(content)
    print(f"Day {DAY_NUMBER}, Part 2 solution: {result}")


if __name__ == "__main__":
    main()
