from numba import njit

MASK = (1 << 24) - 1  # 16777215 or 0xFFFFFF


@njit  # Use numba for speedup
def calc_next_secret(n):
    """Calculate next secret number using the monkey's algorithm.Uses bitwise operations."""
    # Each step: multiply/divide, XOR with original, mask to 24 bits
    n = (n ^ (n << 6)) & MASK  # Multiply by 64 (2^6)
    n = (n ^ (n >> 5)) & MASK  # Divide by 32 (2^5)
    n = (n ^ (n << 11)) & MASK  # Multiply by 2048 (2^11)
    return n


def split_into_chunks(items, num_chunks):
    """Split items into roughly equal chunks for parallel processing."""
    chunk_size = max(1, len(items) // num_chunks)
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def parse_input(content):
    return [int(line) for line in content.strip().split("\n")]
