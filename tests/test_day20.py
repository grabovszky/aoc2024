from solutions.day20.part1 import solve_part1
from solutions.day20.part2 import solve_part2

test_input = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


def test_part1():
    assert solve_part1(test_input) == 0


def test_part2():
    assert solve_part2(test_input) == 0
