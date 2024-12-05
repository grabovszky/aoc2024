def parse_input(content):
    reports = []

    for line in content.strip().splitlines():
        levels = [int(num) for num in line.strip().split()]
        if levels:
            reports.append(levels)

    return reports


def is_safe(levels):
    if len(levels) < 2:
        return True  # A single level is considered safe

    differences = [levels[i] - levels[i - 1] for i in range(1, len(levels))]

    # Check if all differences are positive (increasing) or all negative (decreasing)
    is_increasing = all(d > 0 for d in differences)
    is_decreasing = all(d < 0 for d in differences)

    if not (is_increasing or is_decreasing):
        return False

    # Check that adjacent levels differ by at least one and at most three
    if not all(1 <= abs(d) <= 3 for d in differences):
        return False

    return True
