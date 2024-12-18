from solutions.day18.part1 import solve_part1
from solutions.day18.part2 import solve_part2

TEST_INPUT = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def test_part1():
    assert solve_part1(TEST_INPUT.strip(), test_mode=True) == 22


def test_part2():
    assert solve_part2(TEST_INPUT.strip(), test_mode=True) == "6,1"
