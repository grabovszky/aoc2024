from solutions.day10.part1 import solve_part1
from solutions.day10.part2 import solve_part2


TEST_INPUT = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def test_part1():
    assert solve_part1(TEST_INPUT.strip()) == 36


def test_part2():
    assert solve_part2(TEST_INPUT.strip()) == 81
