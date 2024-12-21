NUMERIC_PAD = {
    c: (row, col)
    for row, line in enumerate("789\n456\n123\n 0A".splitlines())
    for col, c in enumerate(line)
    if c != " "
}

DIRECTIONAL_PAD = {
    c: (row, col)
    for row, line in enumerate(" ^A\n<v>".splitlines())
    for col, c in enumerate(line)
    if c != " "
}

cache = {}


def find_paths(keypad, start_pos, target):
    """
    Find shortest paths from start position to target letter.
    Uses directional pathfinding - moves towards target in both dimensions.
    """
    to_check = [(start_pos, "")]
    target_pos = keypad[target]

    while to_check:
        pos, path = to_check.pop()

        if pos == target_pos:
            yield path
            continue

        # Try horizontal movement first
        col_diff = target_pos[1] - pos[1]
        if col_diff:
            direction = ">" if col_diff > 0 else "<"
            new_pos = (pos[0], pos[1] + (1 if col_diff > 0 else -1))
            if new_pos in keypad.values():
                to_check.append((new_pos, path + direction))

        # Then try vertical movement
        row_diff = target_pos[0] - pos[0]
        if row_diff:
            direction = "v" if row_diff > 0 else "^"
            new_pos = (pos[0] + (1 if row_diff > 0 else -1), pos[1])
            if new_pos in keypad.values():
                to_check.append((new_pos, path + direction))


def get_min_sequence_length(keypad, code, robots):
    """
    Calculate minimum sequence length using recursive robot chain.
    Each robot generates sequences for the next robot in chain.
    Uses caching to avoid recalculating common subsequences.
    """
    cache_key = (len(keypad), code, robots)
    if cache_key in cache:
        return cache[cache_key]

    # Base case: last robot just types the code directly
    if robots == 0:
        cache[cache_key] = len(code)
        return len(code)

    current_pos = keypad["A"]  # All robots start at 'A'
    total_length = 0
    next_robots = robots - 1

    # For each letter, find shortest path and generate sequence for next robot
    for letter in code:
        min_length = min(
            get_min_sequence_length(DIRECTIONAL_PAD, seq + "A", next_robots)
            for seq in find_paths(keypad, current_pos, letter)
        )
        total_length += min_length
        current_pos = keypad[letter]

    cache[cache_key] = total_length
    return total_length


def calculate_complexity(code, sequence_length):
    """Calculate complexity: numeric part * sequence length."""
    numeric_part = int("".join(c for c in code if c.isdigit()))
    return sequence_length * numeric_part
