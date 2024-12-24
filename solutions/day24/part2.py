from solutions.common import read_input
from .utils import parse_input, find_incorrect_wires


def solve_part2(content):
    """Find wires that need to be swapped to fix the circuit."""
    _, gates = parse_input(content)
    wrong_wires = find_incorrect_wires(gates)
    return ",".join(sorted(wrong_wires))


def main():
    return solve_part2(read_input(24))


if __name__ == "__main__":
    main()
