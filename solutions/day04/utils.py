# solutions/day04/utils.py


def parse_grid(content_lines):
    letters = {}
    x_positions = []
    a_positions = []

    for row_idx, line in enumerate(content_lines):
        for col_idx, char in enumerate(line):
            position = complex(
                col_idx, row_idx
            )  # Use complex numbers to represent positions
            letters[position] = char
            if char == "X":
                x_positions.append(position)
            if char == "A":
                a_positions.append(position)
    return letters, x_positions, a_positions


def count_xmas_occurrences(letters, x_positions):
    directions = [
        complex(1, 0),  # Right
        complex(-1, 0),  # Left
        complex(0, 1),  # Down
        complex(0, -1),  # Up
        complex(1, 1),  # Down-Right
        complex(-1, 1),  # Down-Left
        complex(1, -1),  # Up-Right
        complex(-1, -1),  # Up-Left
    ]

    count = 0
    for x_pos in x_positions:
        for direction in directions:
            positions = [
                x_pos + i * direction for i in range(1, 4)
            ]  # Positions for 'M', 'A', 'S'
            letters_in_direction = "".join(letters.get(pos, "") for pos in positions)
            if letters_in_direction == "MAS":
                count += 1
    return count


def count_x_mas_occurrences(letters, a_positions):
    # Relative positions around 'A' to form an 'X' shape
    x_offsets = [
        complex(-1, -1),
        complex(1, -1),
        complex(1, 1),
        complex(-1, 1),
    ]

    count = 0
    for a_pos in a_positions:
        surrounding_letters = "".join(
            letters.get(a_pos + offset, "") for offset in x_offsets
        )
        # Check for patterns where 'MAS' forms an 'X' shape around 'A'
        valid_patterns = {"MMSS", "MSSM", "SSMM", "SMMS"}
        if surrounding_letters in valid_patterns:
            count += 1
    return count
