import re


def extract_mul_instructions(content):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    mul_instructions = re.findall(pattern, content)

    return mul_instructions


def extract_instructions_with_control(content):
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    instructions = re.findall(pattern, content)

    return instructions
