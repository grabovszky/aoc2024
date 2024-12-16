from heapq import heappush, heappop
from collections import defaultdict

DIRECTIONS = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
TURNS = {
    "L": "LUD",
    "R": "RUD",
    "U": "ULR",
    "D": "DLR",
}  # Valid turns from each direction


def parse_input(input_str):
    """Parse input into grid and find start/end positions."""
    grid = [list(x) for x in input_str.strip().split("\n")]

    # Find S and E positions
    start = end = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "S":
                start = (x, y)
            if cell == "E":
                end = (x, y)

    return grid, start, end


def find_paths(grid, start, end):
    """Find all shortest paths through maze using Dijkstra.
    Returns distances and predecessors for path reconstruction.
    """
    queue = [(0, (*start, "R"))]  # Start facing right
    seen = set()
    dist = defaultdict(lambda: float("inf"))
    dist[(*start, "R")] = 0
    prev = defaultdict(list)

    while queue:
        cost, (x, y, heading) = heappop(queue)
        state = (x, y, heading)

        if state in seen:
            continue
        seen.add(state)

        # Try all possible turns
        for new_heading in TURNS[heading]:
            dx, dy = DIRECTIONS[new_heading]
            new_x, new_y = x + dx, y + dy

            if grid[new_y][new_x] == "#":
                continue

            new_cost = cost + (1 if heading == new_heading else 1001)
            new_state = (new_x, new_y, new_heading)

            if new_cost <= dist[new_state]:
                if new_cost < dist[new_state]:
                    prev[
                        new_state
                    ] = []  # Clear previous paths if we found a better one
                dist[new_state] = new_cost
                heappush(queue, (new_cost, new_state))
                prev[new_state].append(state)

    return dist, prev
