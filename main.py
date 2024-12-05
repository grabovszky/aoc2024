import importlib
import argparse
import time


def run_day(day_number, show_time=False):
    day_module = f"solutions.day{day_number:02d}"
    try:
        part1_module = importlib.import_module(f"{day_module}.part1")
        part2_module = importlib.import_module(f"{day_module}.part2")
    except ModuleNotFoundError:
        print(f"Day {day_number:02d} modules not found.")
        return

    print(f"Running Day {day_number:02d} solutions:")
    day_start_time = time.time()

    # Run Part 1
    try:
        if show_time:
            start_time = time.time()
        part1_module.main()
        if show_time:
            part1_time = time.time() - start_time
            print(f"Part 1 completed in {part1_time:.4f} seconds.")
    except Exception as e:
        print(f"Error running Day {day_number:02d} Part 1: {e}")

    # Run Part 2
    try:
        if show_time:
            start_time = time.time()
        part2_module.main()
        if show_time:
            part2_time = time.time() - start_time
            print(f"Part 2 completed in {part2_time:.4f} seconds.")
    except Exception as e:
        print(f"Error running Day {day_number:02d} Part 2: {e}")

    if show_time:
        total_day_time = time.time() - day_start_time
        print(f"Total time for Day {day_number:02d}: {total_day_time:.4f} seconds.\n")


def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code 2024 solutions.")
    parser.add_argument(
        "--day",
        type=int,
        help="Specify the day to run (1-25). If not specified, runs all days.",
    )
    parser.add_argument(
        "--time",
        action="store_true",
        help="Display execution time for each part.",
    )
    args = parser.parse_args()

    overall_start_time = time.time()

    if args.day:
        run_day(args.day, show_time=args.time)
    else:
        for day_number in range(1, 26):
            run_day(day_number, show_time=args.time)

    if args.time:
        total_time = time.time() - overall_start_time
        print(f"Total execution time: {total_time:.4f} seconds.")


if __name__ == "__main__":
    main()
