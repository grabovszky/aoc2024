from solutions.common import read_input
from .utils import parse_input, Computer


def find_matching_a(program, target):
    """Find initial A value that produces target output sequence."""

    def search(a=0, depth=0):
        if depth == len(target):
            return a

        # Try all possible next digits (0-7)
        for i in range(8):
            value = a * 8 + i
            computer = Computer(program, value)
            output = computer.run()

            # Check if this digit matches target
            if output and output[0] == target[depth]:
                if result := search(value, depth + 1):
                    return result
        return 0

    return search()


def solve_part2(content):
    """Find A value that generates reversed program as output."""
    _, _, _, program = parse_input(content)
    target = program[::-1]  # Reverse program is our target output
    return find_matching_a(program, target)


def main():
    return solve_part2(read_input(17))


if __name__ == "__main__":
    main()
