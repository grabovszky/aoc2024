from solutions.common import read_input
from collections import deque
from .utils import parse_input, calculate_gps_score, DIRECTIONS


def expand_grid(grid):
    """Convert single-width grid to double-width grid."""
    expanded = []
    pos = None
    for r, line in enumerate(grid):
        row = []
        for c, p in enumerate(line):
            if p == "#":
                row.extend(["#", "#"])
            elif p == "O":
                row.extend(["[", "]"])
            elif p == ".":
                row.extend([".", "."])
            elif p == "@":
                row.extend(["@", "."])
                pos = (r, c * 2)
        expanded.append(row)
    return expanded, pos


def get_train(grid, move, pos):
    """Get all boxes that should move, using BFS to handle double-width boxes."""
    q = deque([pos])
    seen = set()
    cur_train = []
    dr, dc = DIRECTIONS[move]

    while q:
        r, c = q.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))

        if grid[r][c] == ".":
            continue
        elif grid[r][c] == "#":
            return False, []

        cur_train.append((r, c))
        cur_p = grid[r][c]
        assert cur_p in {"[", "]", "@"}

        if cur_p == "[" and move != ">":
            if (r, c + 1) not in seen:
                q.append((r, c + 1))
        elif cur_p == "]" and move != "<":
            if (r, c - 1) not in seen:
                q.append((r, c - 1))

        q.append((r + dr, c + dc))

    return True, cur_train


def solve_part2(content):
    """Solve part 2: Calculate GPS score after moving boxes in double-width grid."""
    grid, moves, _ = parse_input(content)

    # Convert to double-width grid
    grid, pos = expand_grid(grid)

    # Process each move
    for move in moves:
        ok, cur_train = get_train(grid, move, pos)
        if not ok:
            continue

        dr, dc = DIRECTIONS[move]
        for pr, pc in cur_train[::-1]:
            if grid[pr][pc] == "@":
                pos = (pr + dr, pc + dc)
            grid[pr + dr][pc + dc] = grid[pr][pc]
            grid[pr][pc] = "."

    return calculate_gps_score(grid, box_char="[")


def main():
    content = read_input(15)
    result = solve_part2(content)
    return result


if __name__ == "__main__":
    main()
