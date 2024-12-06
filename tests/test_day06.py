from solutions.day06.part1 import solve_part1
from solutions.day06.part2 import solve_part2

TEST_DATA = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def test_part1():
    expected_result = 41
    assert solve_part1(TEST_DATA) == expected_result


def test_part2():
    expected_result = 6
    assert solve_part2(TEST_DATA) == expected_result
