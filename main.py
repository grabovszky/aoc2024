import importlib
import argparse


def run_day(day_number):
    day_module = f"solutions.day{day_number:02d}"
    try:
        part1_module = importlib.import_module(f"{day_module}.part1")
        part2_module = importlib.import_module(f"{day_module}.part2")
    except ModuleNotFoundError:
        print(f"Day {day_number:02d} modules not found.")
        return

    print(f"Running Day {day_number:02d} solutions:")

    # Run Part 1
    try:
        part1_module.main()
    except Exception as e:
        print(f"Error running Day {day_number:02d} Part 1: {e}")

    # Run Part 2
    try:
        part2_module.main()
    except Exception as e:
        print(f"Error running Day {day_number:02d} Part 2: {e}")


def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code 2024 solutions.")
    parser.add_argument(
        "--day",
        type=int,
        help="Specify the day to run (1-25). If not specified, runs all days.",
    )
    args = parser.parse_args()

    if args.day:
        run_day(args.day)
    else:
        for day_number in range(1, 26):
            run_day(day_number)


if __name__ == "__main__":
    main()
