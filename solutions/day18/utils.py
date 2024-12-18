import heapq


def parse_input(input_str, test_mode=False):
    """Parse input into list of byte coordinates (x,y) and determine grid size."""
    bytes = []
    max_coord = 0
    for line in input_str.strip().split("\n"):
        y, x = map(int, line.split(","))
        bytes.append((x, y))
        max_coord = max(max_coord, x, y)

    # For test input use exact size, for real input use 71
    size_space = max_coord + 1 if test_mode else 71
    return bytes, size_space


def find_shortest_path(corrupted, size_space):
    """Find shortest path from (0,0) to (size-1,size-1) using Dijkstra's algorithm."""
    # Possible movement directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Initialize data structures
    pq = [(0, 0, 0)]  # (distance, row, col)
    visited = set()
    in_heap = {(0, 0, 0)}

    while pq:
        dist, r, c = heapq.heappop(pq)
        visited.add((r, c))

        # Try all possible moves
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Skip if already visited
            if (nr, nc) in visited:
                continue

            # Check if reached target
            if (nr, nc) == (size_space - 1, size_space - 1):
                return dist + 1

            # Check if move is valid
            if is_valid_move((nr, nc), corrupted, size_space):
                next_state = (dist + 1, nr, nc)
                if next_state not in in_heap:
                    heapq.heappush(pq, next_state)
                    in_heap.add(next_state)

    return size_space * size_space + 1  # No path found


def is_valid_move(pos, corrupted, size_space):
    """Check if a position is valid (within bounds and not corrupted)."""
    x, y = pos
    return 0 <= x < size_space and 0 <= y < size_space and pos not in corrupted
