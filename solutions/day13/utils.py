import re
from collections import namedtuple

Machine = namedtuple("Machine", ["a", "b", "prize"])


def parse_input(content):
    """Parse input into list of machines with button configurations.

    Each machine has:
    - Button A position (x, y)
    - Button B position (x, y)
    - Prize position (x, y)

    Returns a list of Machine objects, each containing these three coordinate pairs.
    """
    numbers = [int(x) for x in re.findall(r"\d+", content)]

    # Process numbers in groups of 6
    machines = []
    for i in range(0, len(numbers), 6):
        # Get coordinates for one machine
        button_a = (numbers[i], numbers[i + 1])  # First button position
        button_b = (numbers[i + 2], numbers[i + 3])  # Second button position
        prize = (numbers[i + 4], numbers[i + 5])  # Prize position

        # Create Machine object and add to list
        machines.append(Machine(button_a, button_b, prize))

    return machines


def solve_machine(machine, translate=False):
    """Solve single machine using Cramer's rule."""
    # Unpack machine configuration
    (ax, ay), (bx, by), (px, py) = machine

    # Apply translation for part 2
    if translate:
        px += 10**13
        py += 10**13

    # Calculate determinants for Cramer's rule
    D = ax * by - ay * bx
    if D == 0:
        return 0

    # Find number of button presses needed
    Na = px * by - py * bx
    Nb = ax * py - ay * px

    # Check if solution exists with integer presses
    if Na % D == 0 and Nb % D == 0:
        a, b = Na // D, Nb // D
        if a >= 0 and b >= 0:  # Only positive solutions are valid
            return 3 * a + b

    return 0


def solve_all(machines, translate=False):
    return sum(solve_machine(m, translate) for m in machines)
