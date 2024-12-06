from solutions.common import read_input
from .utils import parse_input, simulate_guard


def solve_part2(content):
    m, g = parse_input(content)

    # First, find the guard's original path
    visited_positions = simulate_guard(m, g)

    # We'll consider only the positions visited by the guard
    visited_positions = list(visited_positions)
    loops = 0

    # Simple logger to see progress
    total_positions = len(visited_positions)
    print(f"Checking {total_positions} positions for possible loops...")

    for i, pos in enumerate(visited_positions, start=1):
        if pos == g:
            continue  # skip guard's start position

        # Print progress every 1000 processed positions
        if i % 1000 == 0:
            print(f"Processed {i}/{total_positions} obstacle positions...")

        if m[pos] == ".":
            original = m[pos]
            m[pos] = "#"  # place a temporary obstacle

            # Re-run simulation
            result = simulate_guard(m, g)
            if result is None:  # loop detected
                loops += 1

            m[pos] = original  # restore original tile

    return loops


def main():
    DAY_NUMBER = 6
    content = read_input(DAY_NUMBER)
    result = solve_part2(content)
    return result


if __name__ == "__main__":
    main()
