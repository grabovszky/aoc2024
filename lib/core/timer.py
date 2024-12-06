import time
from dataclasses import dataclass
from typing import Optional


@dataclass
class TimingResult:
    elapsed: float
    start_time: float
    end_time: float


class Timer:
    def __init__(self):
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None

    def start(self) -> None:
        self.start_time = time.time()

    def stop(self) -> TimingResult:
        self.end_time = time.time()
        if self.start_time is None:
            raise RuntimeError("Timer was never started")
        
        return TimingResult(
            elapsed=self.end_time - self.start_time,
            start_time=self.start_time,
            end_time=self.end_time
        ) 