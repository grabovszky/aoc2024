DIRECTIONS = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}


def parse_input(input_str):
    """Parse input into grid, moves list, and starting position."""
    grid_str, moves_str = input_str.split("\n\n")

    # Parse grid and find robot position
    grid = []
    robot_pos = None
    for r, line in enumerate(grid_str.split("\n")):
        grid.append(list(line))  # Convert string to list of chars
        if "@" in line:
            robot_pos = (r, line.index("@"))

    # Parse moves, ignoring newlines
    moves = [m for line in moves_str.split("\n") for m in line]

    return grid, moves, robot_pos


def calculate_gps_score(grid, box_char="O"):
    """Calculate GPS score for boxes.
    Score = sum of (100 * row + col) for each box position
    """
    score = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == box_char:
                score += 100 * r + c
    return score
