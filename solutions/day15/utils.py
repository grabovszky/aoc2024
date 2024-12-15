DIRECTIONS = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}


def parse_input(input_str):
    """Parse input into grid, moves list, and starting position."""
    wmap, move = input_str.split("\n\n")
    grid = []
    pos = None

    for r, line in enumerate(wmap.split("\n")):
        row = []
        for c, p in enumerate(line):
            row.append(p)
            if p == "@":
                pos = (r, c)
        grid.append(row)

    moves = [m for line in move.split("\n") for m in line]
    return grid, moves, pos


def calculate_gps_score(grid, box_char="O"):
    score = 0
    for r, row in enumerate(grid):
        for c, p in enumerate(row):
            if p == box_char:
                score += 100 * r + c
    return score
