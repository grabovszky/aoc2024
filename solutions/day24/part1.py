from solutions.common import read_input
from .utils import parse_input, simulate_circuit, get_output_value


def solve_part1(content):
    """Simulate circuit and get decimal output from z-wires."""
    values, gates = parse_input(content)
    final_values = simulate_circuit(values, gates)
    return get_output_value(final_values)


def main():
    return solve_part1(read_input(24))


if __name__ == "__main__":
    main()
