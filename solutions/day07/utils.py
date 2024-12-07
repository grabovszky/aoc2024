from typing import List, Tuple, Iterator
from multiprocessing import Pool
from itertools import product


def parse_input(content):
    equations = []

    for line in content.strip().splitlines():
        target_str, nums_str = line.split(":")
        target = int(target_str.strip())
        nums = [int(n) for n in nums_str.strip().split()]
        equations.append((target, nums))

    return equations


def evaluate(nums, ops):
    result = nums[0]

    for op, num in zip(ops, nums[1:]):
        if op == "+":
            result += num
        elif op == "*":
            result *= num
        else:  # op == "||"
            result = int(f"{result}{num}")

    return result


def generate_all_ops(n, allow_concat):
    ops = ["+", "*"]
    if allow_concat:
        ops.append("||")
    return product(ops, repeat=n - 1)


def check_equation(args):
    target, nums, allow_concat = args

    # Check if an equation can be solved, return target if yes, 0 if no
    if len(nums) == 1:
        return target if nums[0] == target else 0

    for ops in generate_all_ops(len(nums), allow_concat):
        if evaluate(nums, ops) == target:
            return target
    return 0


def solve(equations, allow_concat=False):
    # Prepare arguments for parallel processing
    args = [(target, nums, allow_concat) for target, nums in equations]

    # Use multiprocessing to check equations in parallel
    with Pool() as pool:
        results = pool.map(check_equation, args)

    return sum(results)
