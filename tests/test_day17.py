from solutions.day17.part1 import solve_part1
from solutions.day17.part2 import solve_part2


def test_part1():
    test_input = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
    assert solve_part1(test_input.strip()) == "4,6,3,5,6,3,5,2,1,0"


def test_part2():
    test_input = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

    assert solve_part2(test_input.strip()) == 117440
