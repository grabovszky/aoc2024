from solutions.day04.part1 import solve_part1
from solutions.day04.part2 import solve_part2


def test_part1():
    test_data = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""

    expected_result = 18
    assert solve_part1(test_data) == expected_result


def test_part2():
    test_data = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""

    expected_result = 9
    assert solve_part2(test_data) == expected_result
