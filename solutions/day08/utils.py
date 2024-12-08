from collections import defaultdict
from itertools import combinations


def parse_input(content):
    grid = content.strip().splitlines()

    # Group antennas by their frequency (character)
    antenna_groups = defaultdict(list)

    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char != ".":
                antenna_groups[char].append((x, y))

    return grid, antenna_groups


def get_antinodes(p1, p2, grid_size, harmonic):
    """Find antinodes for a pair of antennas.

    In part 1 (harmonic=False): antinodes occur at double distance points
    In part 2 (harmonic=True): antinodes occur at all points on the line
    """
    rows, cols = grid_size
    x1, y1 = p1
    x2, y2 = p2
    antinodes = set()

    if not harmonic:
        # Part 1: Check only double distance points on either side
        for x, y in [
            (2 * x2 - x1, 2 * y2 - y1),  # Double distance from p1
            (2 * x1 - x2, 2 * y1 - y2),  # Double distance from p2
        ]:
            if 0 <= x < rows and 0 <= y < cols:
                antinodes.add((x, y))
        return antinodes

    # Part 2: Find all points on the line through p1 and p2
    dx, dy = x2 - x1, y2 - y1

    # Handle vertical and horizontal lines separately
    if dx == 0 and y1 != y2:  # Vertical line
        return {(x, y1) for x in range(rows)}
    if dy == 0 and x1 != x2:  # Horizontal line
        return {(x1, y) for y in range(cols)}

    # For diagonal lines, use parametric form to find points
    max_steps = max(rows, cols)
    for t in range(-max_steps, max_steps):
        x = x1 + t * dx
        y = y1 + t * dy
        if 0 <= x < rows and 0 <= y < cols:
            antinodes.add((int(x), int(y)))

    return antinodes


def find_antinodes(grid, antenna_groups, harmonic=False):
    grid_size = (len(grid), len(grid[0]))
    antinodes = set()

    # Process each group of same-frequency antennas
    for antennas in antenna_groups.values():
        if len(antennas) < 2:  # Need at least 2 antennas to form antinodes
            continue

        # Check each pair of antennas in the group
        for a1, a2 in combinations(antennas, 2):
            antinodes.update(get_antinodes(a1, a2, grid_size, harmonic))

    return antinodes
