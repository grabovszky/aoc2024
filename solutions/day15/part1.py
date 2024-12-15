from solutions.common import read_input
from .utils import parse_input, calculate_gps_score, DIRECTIONS


def move_train(grid, pos, direction):
    """Move a train of boxes in the given direction. Returns success flag and new position."""
    dr, dc = DIRECTIONS[direction]
    cur_train = []

    # Find all boxes that need to move
    tr, tc = pos
    ok = False
    while True:
        if grid[tr][tc] in {"@", "O"}:
            cur_train.append((tr, tc))
        elif grid[tr][tc] == "#":
            break
        else:
            assert grid[tr][tc] == "."
            ok = True
            break
        tr += dr
        tc += dc

    if not ok:
        return False, pos

    # Move the train
    new_pos = pos
    for pr, pc in cur_train[::-1]:
        if grid[pr][pc] == "@":
            new_pos = (pr + dr, pc + dc)
        grid[pr + dr][pc + dc] = grid[pr][pc]
        grid[pr][pc] = "."

    return True, new_pos


def solve_part1(content):
    """Solve part 1: Calculate GPS score after moving boxes in single-width grid."""
    grid, moves, pos = parse_input(content)

    # Process each move
    for move in moves:
        success, pos = move_train(grid, pos, move)

    return calculate_gps_score(grid)


def main():
    content = read_input(15)
    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
