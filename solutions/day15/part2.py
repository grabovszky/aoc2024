from solutions.common import read_input
from collections import deque
from .utils import parse_input, calculate_gps_score, DIRECTIONS


def expand_grid(grid):
    """Convert single-width grid to double-width grid.
    Each cell becomes two cells:
        # -> ##    (wall)
        O -> []    (box)
        . -> ..    (empty)
        @ -> @.    (robot)
    """
    expanded = []
    robot_pos = None

    for r, line in enumerate(grid):
        row = []
        for c, cell in enumerate(line):
            if cell == "#":
                row.extend(["#", "#"])
            elif cell == "O":
                row.extend(["[", "]"])
            elif cell == ".":
                row.extend([".", "."])
            elif cell == "@":
                row.extend(["@", "."])
                robot_pos = (r, c * 2)  # Position in expanded grid
        expanded.append(row)

    return expanded, robot_pos


def find_movable_pieces(grid, pos, move):
    """Find all pieces that need to move together using BFS."""
    dr, dc = DIRECTIONS[move]
    seen = set()
    to_move = []
    queue = deque([pos])

    while queue:
        r, c = queue.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))

        cell = grid[r][c]
        if cell == ".":
            continue
        if cell == "#":
            return False, []

        # Add current position to move list
        to_move.append((r, c))

        # Add connected box part to queue
        if cell == "[" and move != ">":  # Left part of box
            if (r, c + 1) not in seen:
                queue.append((r, c + 1))
        elif cell == "]" and move != "<":  # Right part of box
            if (r, c - 1) not in seen:
                queue.append((r, c - 1))

        # Add next position in movement direction
        queue.append((r + dr, c + dc))

    return True, to_move


def solve_part2(content):
    """Solve part 2: Move robot and double-width boxes."""
    # Parse input and expand grid
    grid, moves, _ = parse_input(content)
    grid, pos = expand_grid(grid)

    # Process moves
    for move in moves:
        can_move, pieces = find_movable_pieces(grid, pos, move)
        if not can_move:
            continue

        # Move all pieces
        dr, dc = DIRECTIONS[move]
        for r, c in pieces[::-1]:
            if grid[r][c] == "@":
                pos = (r + dr, c + dc)
            grid[r + dr][c + dc] = grid[r][c]
            grid[r][c] = "."

    return calculate_gps_score(grid, box_char="[")


def main():
    content = read_input(15)
    return solve_part2(content)


if __name__ == "__main__":
    main()
