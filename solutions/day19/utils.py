from functools import cache, lru_cache
from multiprocessing import Pool
import multiprocessing as mp


def parse_input(content):
    """Parse input into towel patterns and designs."""
    lines = content.strip().split("\n")
    # Sort towels by length (descending) for better performance
    towels = tuple(sorted(lines[0].split(", "), key=len, reverse=True))
    designs = lines[2:]  # Skip the empty line
    return towels, designs


# Pre-calculate minimum towel length
@lru_cache(maxsize=1)
def get_min_towel_length(towels):
    return min(len(t) for t in towels)


@cache
def num_arrangements(design, towels, start=0):
    """Calculate number of possible arrangements for a design."""
    # Early exit if we've reached the end
    if start >= len(design):
        return 1

    # Early exit if remaining length is too short for any towel
    min_len = get_min_towel_length(towels)
    if start + min_len > len(design):
        return 0

    result = 0
    design_slice = design[start:]

    # Try each towel pattern
    for towel in towels:
        if len(towel) > len(design_slice):
            continue

        if design_slice.startswith(towel):
            result += num_arrangements(design, towels, start + len(towel))

    return result


def process_design(args):
    """Process a single design for parallel processing."""
    design, towels = args
    return num_arrangements(design, towels)


def solve_designs_parallel(designs, towels):
    """Solve multiple designs in parallel."""
    # Use optimal number of processes (leave one core free)
    num_processes = max(1, mp.cpu_count() - 1)

    # Create argument tuples for each design
    args = [(design, towels) for design in designs]

    # Process in parallel
    with Pool(num_processes) as pool:
        results = pool.map(process_design, args)

    return results
