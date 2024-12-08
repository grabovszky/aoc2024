from solutions.common import read_input
from .utils import parse_input, find_antinodes


def solve_part2(content):
    grid, antenna_groups = parse_input(content)
    antinodes = find_antinodes(grid, antenna_groups, harmonic=True)
    return len(antinodes)


def main():
    DAY_NUMBER = 8
    content = read_input(DAY_NUMBER)
    result = solve_part2(content)
    return result


if __name__ == "__main__":
    main()
