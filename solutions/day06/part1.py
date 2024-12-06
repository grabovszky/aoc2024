from solutions.common import read_input
from .utils import parse_input, simulate_guard


def solve_part1(content):
    m, g = parse_input(content)
    visited_positions = simulate_guard(m, g)

    # visited_positions won't be None since part1 scenario always ends with guard leaving map
    return len(visited_positions)


def main():
    DAY_NUMBER = 6
    content = read_input(DAY_NUMBER)
    result = solve_part1(content)
    print(f"Day {DAY_NUMBER}, Part 1 solution: {result}")


if __name__ == "__main__":
    main()
