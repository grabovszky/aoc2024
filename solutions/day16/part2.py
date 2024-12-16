from solutions.common import read_input
from .utils import parse_input, find_paths


def count_visited_cells(start, end, dist, prev):
    """Count maximum number of unique cells visited in shortest paths."""
    # Find all end states with best score
    best_cost = min(dist[(*end, h)] for h in "LRUD")
    best_ends = [(end[0], end[1], h) for h in "LRUD" if dist[(*end, h)] == best_cost]

    def trace_path(state, visited):
        """Recursively trace path and collect visited cells."""
        if state not in prev:
            return
        x, y, _ = state
        visited.add((x, y))
        for prev_state in prev[state]:
            trace_path(prev_state, visited)

    # Try all best paths and find the one visiting most cells
    max_visited = 0
    for end_state in best_ends:
        visited = {start}  # Start with start position
        trace_path(end_state, visited)
        max_visited = max(max_visited, len(visited))

    return max_visited


def solve_part2(content):
    """Count cells in shortest path through maze."""
    grid, start, end = parse_input(content)
    dist, prev = find_paths(grid, start, end)
    return count_visited_cells(start, end, dist, prev)


def main():
    return solve_part2(read_input(16))


if __name__ == "__main__":
    main()
