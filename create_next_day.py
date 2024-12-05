#!/usr/bin/env python3

import os
import sys
import shutil
import traceback


def get_next_day_number():
    solutions_dir = os.path.join(os.path.dirname(__file__), "solutions")
    existing_days = [
        int(name[3:])
        for name in os.listdir(solutions_dir)
        if os.path.isdir(os.path.join(solutions_dir, name)) and name.startswith("day")
    ]
    next_day = max(existing_days, default=0) + 1
    if next_day > 25:
        print("All 25 days have already been created.")
        sys.exit(1)
    return next_day


def create_day_structure(day_number):
    try:
        # Keep track of created files and directories for cleanup
        created_dirs = []
        created_files = []

        # Format day number with leading zero
        day_str = f"day{day_number:02d}"

        # Paths
        solutions_dir = os.path.join(os.path.dirname(__file__), "solutions", day_str)
        inputs_dir = os.path.join(os.path.dirname(__file__), "inputs")
        tests_dir = os.path.join(os.path.dirname(__file__), "tests")

        # Create directories
        os.makedirs(solutions_dir, exist_ok=False)
        created_dirs.append(solutions_dir)

        os.makedirs(inputs_dir, exist_ok=True)  # Assume inputs/ already exists
        os.makedirs(tests_dir, exist_ok=True)  # Assume tests/ already exists

        # Create __init__.py
        init_file = os.path.join(solutions_dir, "__init__.py")
        open(init_file, "a").close()
        created_files.append(init_file)

        # Create utils.py
        utils_file = os.path.join(solutions_dir, "utils.py")
        open(utils_file, "a").close()
        created_files.append(utils_file)

        # Create part1.py
        part1_file = os.path.join(solutions_dir, "part1.py")
        with open(part1_file, "w") as f:
            f.write(
                f"""from solutions.common import read_input


def solve_part1(content):
    # Implement solution logic here
    pass


def main():
    DAY_NUMBER = {day_number}
    content = read_input(DAY_NUMBER)
    result = solve_part1(content)
    print(f"Day {{DAY_NUMBER}}, Part 1 solution: {{result}}")


if __name__ == "__main__":
    main()
"""
            )
        created_files.append(part1_file)

        # Create part2.py
        part2_file = os.path.join(solutions_dir, "part2.py")
        with open(part2_file, "w") as f:
            f.write(
                f"""from solutions.common import read_input


def solve_part2(content):
    # Implement solution logic here
    pass


def main():
    DAY_NUMBER = {day_number}
    content = read_input(DAY_NUMBER)
    result = solve_part2(content)
    print(f"Day {{DAY_NUMBER}}, Part 2 solution: {{result}}")


if __name__ == "__main__":
    main()
"""
            )
        created_files.append(part2_file)

        # Create input file
        input_file = os.path.join(inputs_dir, f"{day_str}.txt")
        open(input_file, "a").close()  # Creates an empty input file
        created_files.append(input_file)

        # Create test file
        test_file = os.path.join(tests_dir, f"test_{day_str}.py")
        with open(test_file, "w") as f:
            f.write(
                f"""from solutions.{day_str}.part1 import solve_part1
from solutions.{day_str}.part2 import solve_part2


def test_part1():
    test_data = \"\"\"\"\"\"  # Add test data here
    expected_result = None  # Replace with expected result
    assert solve_part1(test_data) == expected_result


def test_part2():
    test_data = \"\"\"\"\"\"  # Add test data here
    expected_result = None  # Replace with expected result
    assert solve_part2(test_data) == expected_result
"""
            )
        created_files.append(test_file)

        print(f"Day {day_number:02d} structure created successfully.")

    except Exception as e:
        # Print the error message
        print(f"An error occurred while creating Day {day_number:02d}: {e}")
        traceback.print_exc()

        # Clean up created files
        for file_path in created_files:
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except OSError as file_err:
                print(f"Error deleting file {file_path}: {file_err}")

        # Clean up created directories
        for dir_path in created_dirs:
            try:
                shutil.rmtree(dir_path)
                print(f"Deleted directory: {dir_path}")
            except OSError as dir_err:
                print(f"Error deleting directory {dir_path}: {dir_err}")

        sys.exit(1)


def main():
    next_day_number = get_next_day_number()
    create_day_structure(next_day_number)


if __name__ == "__main__":
    main()
