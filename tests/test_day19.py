from solutions.day19.part1 import solve_part1
from solutions.day19.part2 import solve_part2

TEST_INPUT = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


def test_part1():
    assert solve_part1(TEST_INPUT.strip()) == 6


def test_part2():
    assert solve_part2(TEST_INPUT.strip()) == 16
