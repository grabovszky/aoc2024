from solutions.day02.part1 import solve_part1
from solutions.day02.part2 import solve_part2

TEST_DATA = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def test_part1():
    expected_result = 2
    assert solve_part1(TEST_DATA) == expected_result


def test_part2():
    expected_result = 4
    assert solve_part2(TEST_DATA) == expected_result
