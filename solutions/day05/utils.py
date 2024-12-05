from collections import defaultdict
import functools


def parse_input(content):
    sections = content.strip().split("\n\n")
    rules_section = sections[0]
    updates_section = sections[1]

    rules = defaultdict(list)
    for rule in rules_section.strip().split():
        a_str, b_str = rule.split("|")
        a, b = int(a_str), int(b_str)
        rules[a].append(b)

    updates = []
    for update_line in updates_section.strip().splitlines():
        pages = [int(page) for page in update_line.strip().split(",")]
        updates.append(pages)

    return rules, updates


def compare_factory(rules):
    def compare(a, b):
        if b in rules[a]:
            return -1  # a must come before b
        if a in rules[b]:
            return 1  # b must come before a
        return 0  # No specific order between a and b

    return compare


def solve(content, condition):
    rules, updates = parse_input(content)
    compare = compare_factory(rules)

    total = 0
    for update in updates:
        sorted_update = sorted(update, key=functools.cmp_to_key(compare))
        if condition(update, sorted_update):
            middle_page = sorted_update[len(sorted_update) // 2]
            total += middle_page
    return total
