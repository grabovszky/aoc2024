from collections import defaultdict


def parse_input(content):
    m = {}
    guard_pos = None
    im = 1j  # imaginary unit for coordinates

    lines = content.strip().splitlines()

    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            p = i + j * im
            if char == "^":
                guard_pos = p
                m[p] = "."
            else:
                m[p] = char
    return m, guard_pos


def simulate_guard(m, start):
    direction = -1j  # up
    visited_positions = {start}
    visited_states = {(start, direction)}

    # Simulation loop
    while True:
        next_pos = start + direction

        # If next_pos not in m, guard leaves the map
        if next_pos not in m:
            return visited_positions

        if m[next_pos] == "#":  # obstacle ahead, turn right
            # Turning right by multiplying direction by 1j
            # direction order: up(-1j)->right(1)->down(1j)->left(-1)->up(-1j)
            direction *= 1j
        else:
            # Move forward
            start = next_pos
            visited_positions.add(start)

            # Check if we have seen this (pos, direction) before => loop
            state = (start, direction)
            if state in visited_states:
                return None  # Loop detected
            visited_states.add(state)
