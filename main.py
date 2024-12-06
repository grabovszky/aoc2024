import importlib
import argparse
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()


def run_part(day_number, part_number, show_time, module):
    part_name = f"Part {part_number}"
    console.print(
        f":runner: [yellow]Running Day {day_number:02d} {part_name}...[/yellow]"
    )

    result = None
    try:
        if show_time:
            start_time = time.time()
        result = module.main()
        if show_time:
            elapsed = time.time() - start_time
    except Exception as e:
        console.print(
            f":x: [red]Error running Day {day_number:02d} {part_name}: {e}[/red]"
        )
    else:
        console.print(":sparkles: [green]Completed successfully![/green]")
        if result is not None:
            panel_style = "bright_green"
            title_emoji = ":star:"

            console.print()
            console.print(
                Panel(
                    Text(f"{part_name} result: {result}", style="bold magenta"),
                    box=box.ROUNDED,
                    title=f"{title_emoji} {part_name}",
                    subtitle="AOC 2024 :christmas_tree:",
                    style=panel_style,
                    expand=False,
                )
            )
            console.print()
        else:
            console.print("[red]No result returned[/red]")

        if show_time:
            console.print(f"[dim]{part_name} time: {elapsed:.4f} s[/dim]")

    return result


def run_day(day_number, show_time=False):
    day_module = f"solutions.day{day_number:02d}"
    try:
        part1_module = importlib.import_module(f"{day_module}.part1")
        part2_module = importlib.import_module(f"{day_module}.part2")
    except ModuleNotFoundError:
        console.print(f":x: [red]Day {day_number:02d} modules not found.[/red]")
        return

    # Start Day
    console.print(
        Panel(
            Text(f"Day {day_number:02d}", justify="center", style="bold magenta"),
            box=box.HEAVY,
            expand=True,
        )
    )
    day_start_time = time.time()

    # Run Part 1
    run_part(day_number, 1, show_time, part1_module)
    # Run Part 2
    run_part(day_number, 2, show_time, part2_module)

    if show_time:
        total_day_time = time.time() - day_start_time
        console.print(
            f"[dim]Total time for Day {day_number:02d}: {total_day_time:.4f} seconds.[/dim]\n"
        )
    else:
        console.print()  # Blank line separator if no timing


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
        console.print(f"[dim]Total execution time: {total_time:.4f} seconds.[/dim]")


if __name__ == "__main__":
    main()
