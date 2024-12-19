from functools import cache


def parse_input(content):
    """Parse input into towel patterns and designs."""
    lines = content.strip().split("\n")
    towels = lines[0].split(", ")
    designs = lines[2:]  # Skip the empty line
    return towels, designs


@cache
def num_arrangements(design, towels, start=0):
    """Calculate number of possible arrangements for a design."""
    if start >= len(design):
        return 1

    result = 0
    for towel in towels:
        if design[start : start + len(towel)] == towel:
            result += num_arrangements(design, towels, start + len(towel))
    return result
