import argparse
from dataclasses import dataclass
from typing import Optional
from datetime import datetime
import os


@dataclass
class Args:
    day: Optional[int]
    part: Optional[int]
    time: bool
    perf: bool
    log_level: str
    all: bool


def get_current_or_latest_day() -> int:
    # During December, use current date
    now = datetime.now()
    if now.month == 12 and 1 <= now.day <= 25:
        return now.day

    # Otherwise find the latest implemented day
    solutions_dir = "solutions"
    latest_day = 0

    if os.path.exists(solutions_dir):
        for dir_name in os.listdir(solutions_dir):
            if dir_name.startswith("day"):
                try:
                    day_num = int(dir_name[3:])
                    latest_day = max(latest_day, day_num)
                except ValueError:
                    continue

    return latest_day or 1  # Default to day 1 if no solutions found


def parse_args() -> Args:
    parser = argparse.ArgumentParser(description="Run Advent of Code 2024 solutions.")
    parser.add_argument(
        "--day",
        type=int,
        help="Specify the day to run (1-25). If not specified, runs current/latest day.",
    )
    parser.add_argument(
        "--part",
        type=int,
        choices=[1, 2],
        help="Specify which part to run (1 or 2). If not specified, runs both parts.",
    )
    parser.add_argument(
        "--time",
        action="store_true",
        help="Display execution time for each part.",
    )
    parser.add_argument(
        "--perf",
        action="store_true",
        help="Display detailed performance metrics (time and memory usage).",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Set the logging level",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all implemented days",
    )

    args = parser.parse_args()

    # If no day specified and not running all days, use current or latest day
    if not args.day and not args.all:
        args.day = get_current_or_latest_day()

    return Args(
        day=args.day if not args.all else None,
        part=args.part,
        time=args.time,
        perf=args.perf,
        log_level=args.log_level,
        all=args.all,
    )
