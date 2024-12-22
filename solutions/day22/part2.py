from multiprocessing import Pool
import multiprocessing as mp
from solutions.common import read_input
from .utils import parse_input, calc_next_secret, split_into_chunks

BASE = 20  # Base for encoding differences (allows -10 to +9)
WINDOW_SIZE = 4
WINDOW_MOD = BASE**WINDOW_SIZE


def process_sequence(initial_secret):
    """Find all unique price difference patterns in a sequence."""
    n = initial_secret
    window = 0
    seen = set()
    patterns = {}

    # Build initial window of differences
    for _ in range(WINDOW_SIZE):
        n_next = calc_next_secret(n)
        window = window * BASE + ((n_next % 10) - (n % 10))
        n = n_next

    # Process remaining sequence
    for _ in range(1996):  # 2000 - WINDOW_SIZE
        if window not in seen:
            patterns[window] = n % 10
            seen.add(window)
        n_next = calc_next_secret(n)
        window = (window * BASE + ((n_next % 10) - (n % 10))) % WINDOW_MOD
        n = n_next

    return patterns


def process_chunk(chunk):
    return [process_sequence(s) for s in chunk]


def solve_part2(content):
    """Find maximum sum of prices with matching difference patterns."""
    secrets = parse_input(content)
    num_processes = max(1, mp.cpu_count() - 1)
    chunks = split_into_chunks(secrets, num_processes)

    with Pool(num_processes) as pool:
        chunk_results = pool.map(process_chunk, chunks)

    patterns = {}
    for chunk in chunk_results:
        for sequence_patterns in chunk:
            for pattern, value in sequence_patterns.items():
                patterns[pattern] = patterns.get(pattern, 0) + value

    return max(patterns.values())


def main():
    return solve_part2(read_input(22))


if __name__ == "__main__":
    main()
