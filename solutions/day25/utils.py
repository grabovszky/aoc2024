def parse_schematic(schematic):
    """
    Convert a schematic into a list of column heights.
    For locks: counts # from top (excluding first row)
    For keys: counts # from bottom (excluding last row)
    """
    # Split into rows and transpose to get columns
    rows = schematic.split("\n")
    columns = list(zip(*rows))

    # Count # symbols in each column
    return [column.count("#") - 1 for column in columns]


def parse_input(content):
    """
    Parse input into lists of lock and key heights.
    Locks have filled top row, keys have filled bottom row.
    """
    locks, keys = [], []

    # Process each schematic
    for schematic in content.strip().split("\n\n"):
        heights = parse_schematic(schematic)

        # First row filled (#) -> lock
        # Last row filled (#) -> key
        if schematic[0] == "#":
            locks.append(heights)
        else:
            keys.append(heights)

    return locks, keys


def can_fit(key, lock):
    """
    Check if key fits lock without overlapping.
    Sum of heights in each column must be <= 5.
    """
    return all(k + l <= 5 for k, l in zip(key, lock))


def count_fitting_pairs(locks, keys):
    """Count how many unique lock/key pairs fit together."""
    return sum(can_fit(key, lock) for key in keys for lock in locks)
