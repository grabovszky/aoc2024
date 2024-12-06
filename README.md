# Advent of Code 2024

This repository contains my solutions for the [Advent of Code 2024](https://adventofcode.com/2024) challenges.

## Requirements

- Python 3.11 or higher
- Pipenv for dependency management

## Setup Instructions

1. **Clone the Repository:**

```bash
git clone https://github.com/grabovszky/aoc2024.git
cd aoc2024
```

2. **Install Dependencies:**

```bash
python scripts/setup.py
```

3. **Activate the Virtual Environment:**

```bash
pipenv shell
```

The setup script will:
- Install all required dependencies
- Set up pre-commit hooks for:
  - Code formatting with black
  - Running tests before commits
  - Checking Python syntax

## Project Structure

- `inputs/`: Contains all the input files for each day's challenge, named as dayXX.txt, where XX is the day number (e.g., day01.txt).
- `main.py`: The main script to run solutions for all days or a specific day.
- `scripts/`:
  - `create_day.py`: A script to automate the creation of a new day's solution structure, including necessary files and directories.
  - `setup.py`: A script to setup the project and install dependencies.
- `lib/`:
  - `core/`: Contains core functionality, such as `Runner` and `Timer` classes.
  - `utils/`: Contains utility functions, such as `argparser` and `logger`.
- `solutions/`:
  - `common.py`: Contains common utility functions, such as `read_input()` for reading input files.
  - `dayXX/`: Each day's solution is in its own directory, where XX is the day number (e.g., day01, day02, etc.).
    - `part1.py`: Solution for Part 1 of the day's challenge.
    - `part2.py`: Solution for Part 2 of the day's challenge.
    - `utils.py`: Helper functions or classes specific to the day.
- `tests/`:
  - `test_dayXX.py`: Contains tests for Day XX's solutions.

## Usage Instructions

### Running Solutions

Before running any script ensure you are in the project's root directory and have activated the virtual environment by runnin `pipenv shell`.

You can run solutions for all days or a specific day using the main.py script.

To run the current day's solutions:

```bash
python main.py
```

To run all implemented days:

```bash
python main.py --all
```

To run with timing information:

```bash
python main.py --time
```

To run a specific day:

```bash
python main.py --day DAY_NUMBER
```

To run a specific part:

```bash
python main.py --day DAY_NUMBER --part PART_NUMBER
```

### Timing Feature

The `main.py` script includes a timing feature to measure the execution time of each part and the total time for each day.

Enable Timing: Use the `--time` flag when running the script.
Output: The script will display execution times for Part 1, Part 2, and the total time for the day.


## Testing

Tests are located in the `tests/` directory and use the pytest framework.

To run all tests:

```bash
pytest
```
To run tests for a specific day:

```bash
pytest tests/test_dayXX.py
```

## Contributing

If you'd like to add a new day's solution or improve existing ones, please follow these steps.

### Adding a New Day's Solution

To streamline the process of adding a new day's solution, use the create_day.py script. This script automates the creation of the necessary files and directories for the next available day.

To create the structure for a new day's challenge:

```bash
python scripts/create_day.py
```

This script will:

1. Determine the next available day number.
2. Create the necessary directories and files, including:
- `solutions/dayXX/`:
  - `__init__.py`
  - `utils.py`
  - `part1.py` (with DAY_NUMBER pre-filled)
  - `part2.py` (with DAY_NUMBER pre-filled)
- `inputs/dayXX.txt`: Empty input file ready for your puzzle input.
- `tests/test_dayXX.py`: Test file with placeholder functions.
3. Populate files with template code.
4. Handle errors gracefully, cleaning up any partially created files or directories if an error occurs.

### Coding Style Guidelines

- Use Python 3.11 or higher.
- Follow PEP 8 coding style guidelines.

### Code Quality Tools

The project uses pre-commit hooks to ensure code quality. These hooks run automatically on commit and include:
- Code formatting with black
- Python syntax checking
- Running tests

You can run the hooks manually without committing:

```bash
# Run all hooks on all files
pipenv run pre-commit run --all-files

# Run specific hook on all files
pipenv run pre-commit run black --all-files

# Run all hooks on staged files
pipenv run pre-commit run
```

The hooks will also run automatically when you try to commit changes. If any hook fails:
1. The commit will be blocked
2. The hooks may modify files (e.g., black formatting)
3. You'll need to stage any changes and try to commit again

### Adding Tests
- Test Functions Individually: Write tests for both solve_part1 and solve_part2 functions.
- Use Clear Test Data: Include example inputs and expected outputs.
- Avoid Duplication: Use fixtures or module-level variables to share test data.

## License

This project is open source and available under the MIT License.