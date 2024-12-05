from solutions.day01.part1 import solve_part1
from solutions.day01.part2 import solve_part2

TEST_DATA = """3   4
4   3
2   5
1   3
3   9
3   3"""


def test_part1():
    expected_result = 11
    assert solve_part1(TEST_DATA) == expected_result


def test_part2():
    expected_result = 31
    assert solve_part2(TEST_DATA) == expected_result
