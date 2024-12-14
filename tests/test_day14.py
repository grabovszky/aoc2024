from solutions.day14.part1 import solve_part1
from solutions.day14.part2 import solve_part2

TEST_INPUT = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""


def test_part1():
    assert solve_part1(TEST_INPUT.strip(), width=11, height=7) == 12


def test_part2():
    """No test case provided in puzzle description."""
    pass
