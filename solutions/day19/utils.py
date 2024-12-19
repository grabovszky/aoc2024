from functools import cache


def parse_input(content):
    """Parse input into towel patterns and designs."""
    lines = content.strip().split("\n")
    # Sort towels by length (descending) for better performance
    # Longer matches first reduce the number of recursive calls
    towels = tuple(sorted(lines[0].split(", "), key=len, reverse=True))
    designs = lines[2:]  # Skip the empty line
    return towels, designs


@cache
def num_arrangements(design, towels, start=0):
    """Calculate number of possible arrangements for a design."""
    # Early exit if we've reached the end
    if start >= len(design):
        return 1

    # Early exit if remaining length is too short for any towel
    if start + min(len(t) for t in towels) > len(design):
        return 0

    result = 0
    design_slice = design[start:]  # Get slice once instead of multiple times

    # Try each towel pattern
    for towel in towels:
        # Skip if towel is longer than remaining design
        if len(towel) > len(design_slice):
            continue

        # Use direct string comparison
        if design_slice.startswith(towel):
            result += num_arrangements(design, towels, start + len(towel))

    return result
