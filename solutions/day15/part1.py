from solutions.common import read_input
from .utils import parse_input, calculate_gps_score, DIRECTIONS


def move_train(grid, pos, direction):
    """Try to move robot and any boxes in its path.

    A "train" is the robot and any boxes that need to be pushed.
    Movement succeeds if there's an empty space at the end of the train.
    """
    dr, dc = DIRECTIONS[direction]
    train = []  # List of positions to move (robot + boxes)

    # Check if movement is possible by looking ahead
    r, c = pos
    while True:
        # Found empty space - movement possible
        if grid[r][c] == ".":
            return True, move_pieces(grid, train, dr, dc)
        # Hit a wall - movement impossible
        if grid[r][c] == "#":
            return False, pos
        # Add robot/box to train and keep looking
        train.append((r, c))
        r += dr
        c += dc


def move_pieces(grid, positions, dr, dc):
    """Move all pieces in the train one step in given direction.
    Returns the robot's new position.
    """
    robot_pos = None
    # Move pieces from back to front to avoid overwriting
    for r, c in positions[::-1]:
        # Remember robot's new position
        if grid[r][c] == "@":
            robot_pos = (r + dr, c + dc)
        # Move piece
        grid[r + dr][c + dc] = grid[r][c]
        grid[r][c] = "."
    return robot_pos


def solve_part1(content):
    """Solve part 1: Move robot and boxes in single-width grid."""
    grid, moves, pos = parse_input(content)

    for move in moves:
        success, pos = move_train(grid, pos, move)

    return calculate_gps_score(grid)


def main():
    content = read_input(15)
    return solve_part1(content)


if __name__ == "__main__":
    main()
