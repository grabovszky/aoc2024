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
pipenv install
```

3. **Activate the Virtual Environment:**

```bash
pipenv shell
```

## Project Structure

- `inputs/`: Contains all the input files for each day's challenge, named as dayXX.txt, where XX is the day number (e.g., day01.txt).
- `main.py`: The main script to run solutions for all days or a specific day.
- `create_day.py`: A script to automate the creation of a new day's solution structure, including necessary files and directories.
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

To run all days:

```bash
python main.py
```

To run all days with timing information:

```bash
python main.py --time
```

To run a specific day:

```bash
python main.py --day DAY_NUMBER
```

Running Individual Parts

```bash
python -m solutions.DAY_NUMBER.PART_NUMBER
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
python create_day.py
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
- Follow PEP 8 coding style guidelines. (Use the included `black` command.)

Format all files:

```bash
black .
```

### Adding Tests
- Test Functions Individually: Write tests for both solve_part1 and solve_part2 functions.
- Use Clear Test Data: Include example inputs and expected outputs.
- Avoid Duplication: Use fixtures or module-level variables to share test data.

## License

This project is open source and available under the MIT License.