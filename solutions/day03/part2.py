from solutions.common import read_input
from .utils import extract_instructions_with_control
import re


def solve_part2(content):
    instructions = extract_instructions_with_control(content)
    total = 0
    enabled = True  # Initially, mul instructions are enabled

    for instr in instructions:
        if instr == "do()":
            enabled = True
        elif instr == "don't()":
            enabled = False
        elif instr.startswith("mul") and enabled:
            # Extract the numbers from the instruction
            numbers = re.findall(r"\d+", instr)
            x, y = map(int, numbers)
            total += x * y
    return total


def main():
    DAY_NUMBER = 3
    content = read_input(DAY_NUMBER)

    result = solve_part2(content)
    return result


if __name__ == "__main__":
    main()
