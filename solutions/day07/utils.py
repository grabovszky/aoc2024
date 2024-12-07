from itertools import product


def parse_input(content):
    lines = content.strip().splitlines()
    equations = []

    for line in lines:
        target_str, nums_str = line.split(":")
        target = int(target_str.strip())
        nums = list(map(int, nums_str.strip().split()))
        equations.append((target, nums))
    return equations


def can_reach_target(nums, target, allow_concat=False):
    """
    Determine if we can insert '+', '*', and optionally '||' between the given numbers (in order)
    to reach the target value. Operators are evaluated left-to-right with no operator precedence.

    If allow_concat is False: only '+' and '*'.
    If allow_concat is True: include '||' as well.
    """

    # If there's only one number, just check it directly
    if len(nums) == 1:
        return nums[0] == target

    # Define available operators
    ops = ["+", "*"]
    if allow_concat:
        ops.append("||")

    operators_slots = len(nums) - 1

    for combo in product(ops, repeat=operators_slots):
        value = nums[0]
        # Apply each operator in order
        for op, num in zip(combo, nums[1:]):
            if op == "+":
                value = value + num
            elif op == "*":
                value = value * num
            elif op == "||":
                # Concatenate as strings, then convert back to int
                value = int(str(value) + str(num))

        if value == target:
            return True

    return False


def solve(equations, allow_concat=False):
    total = 0
    for target, nums in equations:
        if can_reach_target(nums, target, allow_concat):
            total += target
    return total
