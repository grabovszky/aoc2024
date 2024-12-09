from solutions.day09.part1 import solve_part1
from solutions.day09.part2 import solve_part2


TEST_INPUT = """2333133121414131402"""


def test_part1():
    assert solve_part1(TEST_INPUT.strip()) == 1928


def test_part2():
    assert solve_part2(TEST_INPUT.strip()) == 2858
