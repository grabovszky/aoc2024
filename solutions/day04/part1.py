from solutions.common import read_input
from .utils import parse_grid, count_xmas_occurrences


def solve_part1(content):
    content_lines = [
        line.strip() for line in content.strip().splitlines() if line.strip()
    ]
    letters, x_positions, _ = parse_grid(content_lines)
    total_count = count_xmas_occurrences(letters, x_positions)
    return total_count


def main():
    DAY_NUMBER = 4
    content = read_input(DAY_NUMBER)

    result = solve_part1(content)
    print(f"Day {DAY_NUMBER}, Part 1 solution: {result}")


if __name__ == "__main__":
    main()
