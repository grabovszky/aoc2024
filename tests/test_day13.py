from solutions.day13.part1 import solve_part1
from solutions.day13.part2 import solve_part2

TEST_INPUT = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def test_part1():
    assert solve_part1(TEST_INPUT.strip()) == 480


def test_part2():
    assert solve_part2(TEST_INPUT.strip()) == 875318608908
