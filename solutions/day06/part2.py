from multiprocessing import Pool
from solutions.common import read_input
from .utils import parse_input, simulate_guard


def find_loops(m, g, pos):
    # Check if placing an obstacle at pos creates a loop.
    if pos == g or m[pos] != ".":
        return 0

    # Create modified map with new obstacle
    m_copy = m.copy()
    m_copy[pos] = "#"

    # Return 1 if simulation loops, 0 otherwise
    return 1 if simulate_guard(m_copy, g) is None else 0


def solve_part2(content):
    m, g = parse_input(content)

    # Get original path
    path = simulate_guard(m, g)

    # Use multiprocessing to check all positions
    with Pool() as pool:
        results = pool.starmap(find_loops, ((m, g, pos) for pos in path))

    return sum(results)


def main():
    DAY_NUMBER = 6
    content = read_input(DAY_NUMBER)
    result = solve_part2(content)
    return result


if __name__ == "__main__":
    main()
