from solutions.day21.part1 import solve_part1
from solutions.day21.part2 import solve_part2

TEST_INPUT = """029A
980A
179A
456A
379A"""


def test_part1():
    assert solve_part1(TEST_INPUT.strip()) == 126384


def test_part2():
    assert solve_part2(TEST_INPUT.strip()) == 154115708116294
