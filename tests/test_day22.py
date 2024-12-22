from solutions.day22.part1 import solve_part1
from solutions.day22.part2 import solve_part2


def test_part1():
    test_input = """1
10
100
2024"""

    assert solve_part1(test_input.strip()) == 37327623


def test_part2():
    test_input = """1
2
3
2024"""

    assert solve_part2(test_input.strip()) == 23
