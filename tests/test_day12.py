from solutions.day12.part1 import solve_part1
from solutions.day12.part2 import solve_part2


TEST_INPUT = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def test_part1():
    assert solve_part1(TEST_INPUT.strip()) == 1930


def test_part2():
    assert solve_part2(TEST_INPUT.strip()) == 1206
