from solutions.day03.part1 import solve_part1
from solutions.day03.part2 import solve_part2


def test_part1():
    test_data = (
        """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
    )
    expected_result = 161
    assert solve_part1(test_data) == expected_result


def test_part2():
    test_data = (
        """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
    )
    expected_result = 48
    assert solve_part2(test_data) == expected_result
