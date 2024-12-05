from solutions.common import read_input
from .utils import solve


def solve_part2(content):
    return solve(
        content, condition=lambda update, sorted_update: sorted_update != update
    )


def main():
    DAY_NUMBER = 5
    content = read_input(DAY_NUMBER)

    result = solve_part2(content)
    print(f"Day {DAY_NUMBER}, Part 2 solution: {result}")


if __name__ == "__main__":
    main()