from solutions.common import read_input
from .utils import parse_input, compact_disk_part1, compute_checksum


def solve_part1(content):
    files, free_spaces, disk = parse_input(content)
    compacted = compact_disk_part1(disk)
    return compute_checksum(compacted)


def main():
    DAY_NUMBER = 9
    content = read_input(DAY_NUMBER)
    result = solve_part1(content)
    return result


if __name__ == "__main__":
    main()
