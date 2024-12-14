import re
from collections import defaultdict
from math import prod

# Grid dimensions
WIDTH, HEIGHT = 101, 103


def parse_input(content):
    pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    robots = []

    for match in re.findall(pattern, content):
        pos_x, pos_y, vel_x, vel_y = map(int, match)
        position = [pos_x, pos_y]
        velocity = [vel_x, vel_y]
        robots.append([position, velocity])

    return robots


def count_quadrants(robots, width=WIDTH, height=HEIGHT):
    """Count robots in each quadrant after 100 seconds."""
    counts = defaultdict(int)
    mid_x, mid_y = width // 2, height // 2

    for pos, vel in robots:
        # Calculate position after 100 seconds
        x = (pos[0] + vel[0] * 100) % width
        y = (pos[1] + vel[1] * 100) % height

        # Skip robots on middle lines
        if x == mid_x or y == mid_y:
            continue

        # Add to quadrant count
        counts[(x > mid_x, y > mid_y)] += 1

    return prod(counts.values())


def find_pattern_time(robots):
    """Find time when all robots are in different positions."""
    positions = [[p[0], p[1]] for p, _ in robots]  # Current positions
    velocities = [v for _, v in robots]  # Velocities

    for t in range(1, WIDTH * HEIGHT + 1):
        # Update each robot's position
        for i, (pos, vel) in enumerate(zip(positions, velocities)):
            positions[i][0] = (pos[0] + vel[0]) % WIDTH
            positions[i][1] = (pos[1] + vel[1]) % HEIGHT

        # Check if all positions are unique
        if len(set(tuple(p) for p in positions)) == len(robots):
            return t

    return 0
