from collections import deque
from typing import Dict, Set, Tuple

Point = Tuple[int, int]
Grid = Dict[Point, int]

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def parse_input(content: str) -> Tuple[Grid, Set[Point]]:
    grid = {}
    trailheads = set()

    for row, line in enumerate(content.strip().splitlines()):
        for col, height in enumerate(line):
            point = (row, col)
            height = int(height)
            grid[point] = height
            if height == 0:
                trailheads.add(point)

    return grid, trailheads


def get_neighbors(point: Point, height: int, grid: Grid) -> Set[Point]:
    """Get valid neighbors that are exactly one height higher."""
    row, col = point
    neighbors = set()

    for dr, dc in DIRECTIONS:
        next_point = (row + dr, col + dc)
        if grid.get(next_point) == height + 1:
            neighbors.add(next_point)

    return neighbors


def find_reachable_peaks(start: Point, grid: Grid) -> Set[Point]:
    """Find all height-9 points reachable from start (part 1)."""
    peaks = set()
    queue = deque([start])
    seen = {start}

    while queue:
        current = queue.popleft()
        current_height = grid[current]

        if current_height == 9:
            peaks.add(current)
            continue

        for neighbor in get_neighbors(current, current_height, grid):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return peaks


def count_unique_paths(start: Point, grid: Grid) -> int:
    """Count number of unique paths to height 9 (part 2)."""
    paths = 0
    queue = deque([(start,)])

    while queue:
        path = queue.popleft()
        current = path[-1]
        current_height = grid[current]

        if current_height == 9:
            paths += 1
            continue

        for neighbor in get_neighbors(current, current_height, grid):
            if neighbor not in path:  # Avoid cycles
                queue.append(path + (neighbor,))

    return paths
