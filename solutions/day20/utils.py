from heapq import heappush, heappop
from multiprocessing import Pool
import multiprocessing as mp


def parse_input(content):
    """Parse input into grid and start/end positions."""
    grid = []
    start = end = None

    for i, line in enumerate(content.strip().split("\n")):
        row = list(line)
        grid.append(row)
        for j, c in enumerate(row):
            if c == "S":
                start = (i, j)
            elif c == "E":
                end = (i, j)

    return grid, start, end


def bfs(grid, start, end):
    """Find shortest distances from start to all reachable positions using BFS."""
    rows, cols = len(grid), len(grid[0])
    pq = [(0, start[0], start[1])]
    distances = {}
    best_dist = None

    while pq:
        dist, r, c = heappop(pq)

        # Skip if we already found a shorter path to this position
        if (r, c) not in distances:
            distances[(r, c)] = dist
        else:
            continue

        if (r, c) == end:
            best_dist = dist

        # Check all four adjacent positions
        for dr, dc in [(0, 1), (-1, 0), (0, -1), (1, 0)]:  # right, up, left, down
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
                heappush(pq, (dist + 1, nr, nc))

    return distances, best_dist


def process_row(args):
    """
    Process a single row to find valid cheats.

    For each position in the row:
    1. Check if it's a valid starting point (not a wall, reachable from start)
    2. Look for valid end points within max_jump Manhattan distance
    3. Count cheats that save at least 100 steps
    """

    r1, grid, start_dists, end_dists, base_dist, max_jump, rows, cols = args
    count = 0

    # Check each position in the current row
    for c1 in range(1, cols - 1):
        # Skip walls and unreachable positions
        if grid[r1][c1] == "#" or (r1, c1) not in start_dists:
            continue

        # Calculate valid row range for end positions
        r_start = max(1, r1 - max_jump)
        r_end = min(rows - 1, r1 + max_jump + 1)

        # Check potential end positions
        for r2 in range(r_start, r_end):
            # Calculate remaining distance available for column movement
            manhattan_r = abs(r2 - r1)
            remaining_dist = max_jump - manhattan_r
            if remaining_dist < 0:
                continue

            # Calculate valid column range for end positions
            c_start = max(1, c1 - remaining_dist)
            c_end = min(cols - 1, c1 + remaining_dist + 1)

            # Check each potential end position in range
            for c2 in range(c_start, c_end):
                if grid[r2][c2] == "#" or (r2, c2) not in end_dists:
                    continue

                # Calculate total path length with cheat
                cheat_dist = manhattan_r + abs(c2 - c1)
                if cheat_dist <= max_jump:
                    path_with_cheat = (
                        start_dists[(r1, c1)] + cheat_dist + end_dists[(r2, c2)]
                    )
                    if base_dist - path_with_cheat >= 100:
                        count += 1

    return count


def count_saving_cheats(grid, start_dists, end_dists, base_dist, max_jump):
    """Count all cheats that save at least 100 picoseconds using parallel processing."""
    rows, cols = len(grid), len(grid[0])

    # Create arguments for each row to process
    row_args = [
        (r1, grid, start_dists, end_dists, base_dist, max_jump, rows, cols)
        for r1 in range(1, rows - 1)
    ]

    # Use all available cores
    num_processes = max(1, mp.cpu_count())

    # Process rows in parallel and sum results
    with Pool(num_processes) as pool:
        results = pool.map(process_row, row_args)

    return sum(results)
