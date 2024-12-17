import importlib
from typing import Optional, Any
from lib.core.timer import Timer
from lib.core.performance import measure_performance
from lib.utils.logger import Logger


class Runner:
    def __init__(self, show_time: bool = False, show_perf: bool = False):
        self.show_time = show_time
        self.show_perf = show_perf
        self.logger = Logger()
        self.timer = Timer()

    def run_part(self, day_number: int, part_number: int, module) -> Optional[Any]:
        result = None

        with self.logger.running_part(day_number, part_number):
            try:
                if self.show_time or self.show_perf:
                    self.timer.start()

                if self.show_perf:
                    result, metrics = measure_performance(module.main)()
                    self.logger.print_success(
                        result, metrics=metrics, part_number=part_number
                    )
                else:
                    result = module.main()
                    if self.show_time:
                        timing = self.timer.stop()
                        self.logger.print_success(
                            result, elapsed=timing.elapsed, part_number=part_number
                        )
                    else:
                        self.logger.print_success(result, part_number=part_number)

            except Exception as e:
                self.logger.print_error(day_number, part_number, e)

        return result

    def run_day(self, day_number: int, part: Optional[int] = None) -> None:
        day_module = f"solutions.day{day_number:02d}"
        try:
            if part != 2:
                part1_module = importlib.import_module(f"{day_module}.part1")
            if part != 1:
                part2_module = importlib.import_module(f"{day_module}.part2")
        except ModuleNotFoundError:
            self.logger.print_error(day_number, part or 0, "Module not found")
            return

        self.logger.print_day_header(day_number)

        if self.show_time:
            self.timer.start()

        if part != 2:
            self.run_part(day_number, 1, part1_module)
        if part != 1:
            self.run_part(day_number, 2, part2_module)

        if self.show_time:
            timing = self.timer.stop()
            self.logger.print_timing(
                f"Total time for Day {day_number:02d}", timing.elapsed
            )
