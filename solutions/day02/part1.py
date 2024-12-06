from solutions.common import read_input
from .utils import parse_input, is_safe


def solve_part1(content):
    reports = parse_input(content)
    safe_reports = sum(1 for report in reports if is_safe(report))
    return safe_reports


def main():
    DAY_NUMBER = 2
    content = read_input(DAY_NUMBER)

    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
