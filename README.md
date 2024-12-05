# Advent of Code 2024

This repository contains my solutions for the [Advent of Code 2024](https://adventofcode.com/2024) challenges.

## Requirements

- Python 3.11 or higher
- Pipenv for dependency management

## Setup Instructions

1. **Clone the Repository:**

```bash
git clone https://github.com/your_username/advent_of_code_2024.git
cd advent_of_code_2024
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

To run a specific day:

```bash
python main.py --day DAY_NUMBER
```

Running Individual Parts

```bash
python -m solutions.DAY_NUMBER.PART_NUMBER
```

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

1. In the `solutions/` directory, create a new folder for the day, following the naming convention `dayXX`, where `XX` is the day number padded with zeros (e.g., day04 for Day 4).
2. Create an `__init__.py` file inside the new directory to make it a Python package.
3. Create Solution Files:
  - `part1.py`: Implement the solution for Part 1.
  - `part2.py`: Implement the solution for Part 2.
  - `utils.py`: (Optional) Add any helper functions or classes specific to the day.
4. Place the day's input file in the `inputs/` directory, named as `dayXX.txt`.
5. In the `tests/` directory, create a test file named `test_dayXX.py`.

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