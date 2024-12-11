from solutions.day11.part1 import solve_part1
from solutions.day11.part2 import solve_part2


TEST_INPUT = """125 17"""


def test_part1():
    assert solve_part1(TEST_INPUT.strip()) == 55312


def test_part2():
    assert solve_part2(TEST_INPUT.strip()) == 65601038650482
