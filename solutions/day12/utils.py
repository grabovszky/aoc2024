from collections import defaultdict


def parse_input(content):
    return [list(line) for line in content.strip().splitlines()]


def find_regions(grid):
    """Find and number all connected regions using DFS."""
    height, width = len(grid), len(grid[0])
    region_map = [[0] * width for _ in range(height)]
    seen = set()
    region_count = 0

    def dfs(x, y):
        if (x, y) in seen:
            return
        seen.add((x, y))
        region_map[y][x] = region_count
        plant = grid[y][x]

        # Check all four directions
        if x > 0 and grid[y][x - 1] == plant:
            dfs(x - 1, y)
        if x < width - 1 and grid[y][x + 1] == plant:
            dfs(x + 1, y)
        if y > 0 and grid[y - 1][x] == plant:
            dfs(x, y - 1)
        if y < height - 1 and grid[y + 1][x] == plant:
            dfs(x, y + 1)

    for y in range(height):
        for x in range(width):
            if (x, y) not in seen:
                dfs(x, y)
                region_count += 1

    return region_map


def get_region(x, y, region_map):
    if 0 <= y < len(region_map) and 0 <= x < len(region_map[0]):
        return region_map[y][x]
    return -1


def calculate_properties(grid, count_corners=False):
    """Calculate total price based on area and perimeter/corners."""
    region_map = find_regions(grid)
    height, width = len(grid), len(grid[0])

    area = defaultdict(int)
    perim = defaultdict(int)
    corners = defaultdict(int)

    for y in range(height):
        for x in range(width):
            region = region_map[y][x]
            area[region] += 1

            if count_corners:
                # Check corners for part 2
                for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    a = get_region(x, y, region_map)
                    b = get_region(x + dx, y, region_map)
                    c = get_region(x, y + dy, region_map)
                    d = get_region(x + dx, y + dy, region_map)
                    if (a != b and a != c) or (a == b and a == c and a != d):
                        corners[region] += 1
            else:
                # Calculate perimeter for part 1
                edges = 4
                if get_region(x - 1, y, region_map) == region:
                    edges -= 2
                if get_region(x, y - 1, region_map) == region:
                    edges -= 2
                perim[region] += edges

    if count_corners:
        return sum(area[r] * corners[r] for r in area)
    return sum(area[r] * perim[r] for r in area)
