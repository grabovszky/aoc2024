from solutions.common import read_input
from .utils import extract_mul_instructions
import re


def solve_part1(content):
    mul_instructions = extract_mul_instructions(content)
    total = 0
    for instr in mul_instructions:
        # Extract the numbers from the instruction
        numbers = re.findall(r"\d+", instr)
        x, y = map(int, numbers)
        total += x * y
    return total


def main():
    DAY_NUMBER = 3
    content = read_input(DAY_NUMBER)

    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
