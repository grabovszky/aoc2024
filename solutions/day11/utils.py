from functools import lru_cache


def parse_input(content):
    return [int(x) for x in content.strip().split()]


@lru_cache(maxsize=None)
def count_stones(number, blinks):
    """Count how many stones a single number will become after n blinks.

    Uses dynamic programming with memoization to avoid recalculating
    the same numbers multiple times.

    Rules:
    1. 0 becomes 1
    2. Even number of digits splits into two numbers
    3. Otherwise multiply by 2024
    """
    # Base case: no more blinks
    if blinks == 0:
        return 1

    # Rule 1: if number is 0, it becomes 1
    if number == 0:
        return count_stones(1, blinks - 1)

    # Rule 2: if even number of digits, split in half
    num_digits = len(str(number))
    if num_digits % 2 == 0:
        # Split number in half
        half_digits = num_digits // 2
        divisor = 10**half_digits
        left = number // divisor
        right = number % divisor

        # Count stones for both halves
        return count_stones(left, blinks - 1) + count_stones(right, blinks - 1)

    # Rule 3: multiply by 2024
    return count_stones(number * 2024, blinks - 1)


def simulate_blinks(stones, num_blinks):
    return sum(count_stones(stone, num_blinks) for stone in stones)
