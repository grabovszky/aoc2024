from solutions.common import read_input
from .utils import parse_input, is_safe


def solve_part2(content):
    reports = parse_input(content)
    safe_reports = 0

    for report in reports:
        if is_safe(report):
            safe_reports += 1
        else:
            # Try removing each level to see if the report becomes safe
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1 :]
                if is_safe(modified_report):
                    safe_reports += 1
                    break
    return safe_reports


def main():
    DAY_NUMBER = 2
    content = read_input(DAY_NUMBER)

    result = solve_part2(content)
    print(f"Day {DAY_NUMBER}, Part 2 solution: {result}")


if __name__ == "__main__":
    main()
