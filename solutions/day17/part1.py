from solutions.common import read_input
from .utils import parse_input, Computer


def solve_part1(content):
    """Run program with initial register values and get output."""
    a, b, c, program = parse_input(content)
    computer = Computer(program, a, b, c)
    output = computer.run()
    return ",".join(str(n) for n in output)


def main():
    return solve_part1(read_input(17))


if __name__ == "__main__":
    main()
