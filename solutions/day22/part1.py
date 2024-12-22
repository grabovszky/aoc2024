from multiprocessing import Pool
import multiprocessing as mp
from solutions.common import read_input
from .utils import parse_input, calc_next_secret, split_into_chunks


def get_nth_secret(initial, n=2000):
    """Get the nth secret in sequence."""
    for _ in range(n):
        initial = calc_next_secret(initial)
    return initial


def process_chunk(chunk):
    return [get_nth_secret(s) for s in chunk]


def solve_part1(content):
    """Calculate sum of 2000th secret for each initial secret."""
    secrets = parse_input(content)
    num_processes = max(1, mp.cpu_count() - 1)
    chunks = split_into_chunks(secrets, num_processes)

    with Pool(num_processes) as pool:
        results = pool.map(process_chunk, chunks)

    return sum(s for chunk in results for s in chunk)


def main():
    return solve_part1(read_input(22))


if __name__ == "__main__":
    main()
