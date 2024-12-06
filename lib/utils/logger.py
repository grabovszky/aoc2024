from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.spinner import Spinner
from rich import box
from typing import Optional, Any
from contextlib import contextmanager

console = Console()

class Logger:
    def __init__(self):
        self.live = None
        self.spinner = Spinner('arrow3')

    @staticmethod
    def print_day_header(day_number: int) -> None:
        console.print(
            Panel(
                Text(f"Day {day_number:02d}", justify="center", style="bold magenta"),
                box=box.HEAVY,
                expand=True,
            )
        )

    @contextmanager
    def running_part(self, day_number: int, part_number: int):
        spinner_text = f"Running Day {day_number:02d} Part {part_number}..."
        
        with console.status(f"[yellow]{spinner_text}[/yellow]", spinner='arrow3') as status:
            try:
                yield
            finally:
                status.stop()

    @staticmethod
    def print_error(day_number: int, part_number: int, error: Exception) -> None:
        console.print(
            f":x: [red]Error running Day {day_number:02d} Part {part_number}: {error}[/red]"
        )

    @staticmethod
    def print_success(result: Optional[Any] = None, elapsed: Optional[float] = None, part_number: int = 1) -> None:
        if result is not None:
            panel_style = "bright_green"
            title_emoji = ":star:"

            console.print(
                Panel(
                    Text(f"Part {part_number} result: {result}", style="bold magenta"),
                    box=box.ROUNDED,
                    title=f"{title_emoji} Part {part_number}",
                    subtitle="AOC 2024 :christmas_tree:",
                    style=panel_style,
                    expand=False,
                )
            )
        else:
            console.print("[red]No result returned[/red]")

        if elapsed is not None:
            console.print(f"[dim]Part {part_number} time: {elapsed:.4f} s[/dim]")

    @staticmethod
    def print_timing(message: str, time: float) -> None:
        console.print(f"[dim]{message}: {time:.4f} seconds.[/dim]\n") 