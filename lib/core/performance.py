import functools
import time
import tracemalloc
from dataclasses import dataclass


@dataclass
class PerformanceMetrics:
    execution_time: float  # in seconds
    memory_used: int  # in bytes
    peak_memory: int  # in bytes

    def __str__(self):
        return (
            f"Time: {self.execution_time:.4f}s, "
            f"Memory: {self.memory_used/1024:.1f}KB, "
            f"Peak: {self.peak_memory/1024:.1f}KB"
        )


def measure_performance(func):
    """Decorator to measure execution time and memory usage of a function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        execution_time = time.perf_counter() - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        metrics = PerformanceMetrics(
            execution_time=execution_time, memory_used=current, peak_memory=peak
        )
        return result, metrics

    return wrapper
