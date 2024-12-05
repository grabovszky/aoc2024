from solutions.common import read_input
from .utils import parse_grid, count_x_mas_occurrences


def solve_part2(content):
    content_lines = [
        line.strip() for line in content.strip().splitlines() if line.strip()
    ]
    letters, _, a_positions = parse_grid(content_lines)
    total_count = count_x_mas_occurrences(letters, a_positions)
    return total_count


def main():
    DAY_NUMBER = 4
    content = read_input(DAY_NUMBER)

    result = solve_part2(content)
    print(f"Day {DAY_NUMBER}, Part 2 solution: {result}")


if __name__ == "__main__":
    main()
