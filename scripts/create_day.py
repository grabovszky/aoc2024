from pathlib import Path
from dataclasses import dataclass
from typing import List
import sys


@dataclass
class DayStructure:
    day_number: int
    solutions_dir: Path
    inputs_dir: Path
    tests_dir: Path
    created_files: List[Path]

    @property
    def day_str(self) -> str:
        return f"day{self.day_number:02d}"

    @property
    def day_dir(self) -> Path:
        return self.solutions_dir / self.day_str

    @property
    def input_file(self) -> Path:
        return self.inputs_dir / f"{self.day_str}.txt"

    @property
    def test_file(self) -> Path:
        return self.tests_dir / f"test_{self.day_str}.py"


class DayCreator:
    TEMPLATES = {
        "init": """\"\"\"Day {day_number} solutions\"\"\"
""",
        "part": """from solutions.common import read_input


def solve_part{part}(content):
    # TODO: Implement solution
    pass


def main():
    DAY_NUMBER = {day_number}
    content = read_input(DAY_NUMBER)
    result = solve_part{part}(content)
    return result


if __name__ == "__main__":
    main()
""",
        "utils": """\"\"\"Utility functions for Day {day_number} solutions\"\"\"


def parse_input(content: str):
    # TODO: Implement input parsing
    pass
""",
        "test": """\"\"\"Tests for Day {day_number} solutions\"\"\"
from solutions.{day_str}.part1 import solve_part1
from solutions.{day_str}.part2 import solve_part2


def test_part1():
    test_input = \"\"\"
    # Add test input here
    \"\"\"
    assert solve_part1(test_input.strip()) == None  # TODO: Add expected result


def test_part2():
    test_input = \"\"\"
    # Add test input here
    \"\"\"
    assert solve_part2(test_input.strip()) == None  # TODO: Add expected result
""",
    }

    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.structure = None

    def get_next_day(self) -> int:
        """Find the next available day number"""
        solutions_dir = self.project_root / "solutions"
        existing_days = [
            int(p.name[3:])
            for p in solutions_dir.iterdir()
            if p.is_dir() and p.name.startswith("day")
        ]
        next_day = max(existing_days, default=0) + 1

        if next_day > 25:
            print("Error: All 25 days have already been created.")
            sys.exit(1)

        return next_day

    def initialize_structure(self, day_number: int) -> None:
        """Initialize the day structure"""
        self.structure = DayStructure(
            day_number=day_number,
            solutions_dir=self.project_root / "solutions",
            inputs_dir=self.project_root / "inputs",
            tests_dir=self.project_root / "tests",
            created_files=[],
        )

    def create_directories(self) -> None:
        """Create necessary directories"""
        for directory in [
            self.structure.day_dir,
            self.structure.inputs_dir,
            self.structure.tests_dir,
        ]:
            directory.mkdir(parents=True, exist_ok=True)

    def create_file(self, path: Path, content: str) -> None:
        """Create a file with given content"""
        path.write_text(content)
        self.structure.created_files.append(path)
        print(f"Created: {path.relative_to(self.project_root)}")

    def create_solution_files(self) -> None:
        """Create all solution files"""
        # Create __init__.py
        self.create_file(
            self.structure.day_dir / "__init__.py",
            self.TEMPLATES["init"].format(day_number=self.structure.day_number),
        )

        # Create part1.py and part2.py
        for part in [1, 2]:
            self.create_file(
                self.structure.day_dir / f"part{part}.py",
                self.TEMPLATES["part"].format(
                    day_number=self.structure.day_number, part=part
                ),
            )

        # Create utils.py
        self.create_file(
            self.structure.day_dir / "utils.py",
            self.TEMPLATES["utils"].format(day_number=self.structure.day_number),
        )

        # Create empty input file
        self.create_file(self.structure.input_file, "")

        # Create test file
        self.create_file(
            self.structure.test_file,
            self.TEMPLATES["test"].format(
                day_number=self.structure.day_number, day_str=self.structure.day_str
            ),
        )

    def cleanup(self) -> None:
        """Clean up created files in case of error"""
        for file in self.structure.created_files:
            try:
                file.unlink()
                print(f"Cleaned up: {file.relative_to(self.project_root)}")
            except Exception as e:
                print(f"Error cleaning up {file}: {e}")

        if self.structure.day_dir.exists():
            try:
                self.structure.day_dir.rmdir()
                print(
                    f"Cleaned up: {self.structure.day_dir.relative_to(self.project_root)}"
                )
            except Exception as e:
                print(f"Error cleaning up directory {self.structure.day_dir}: {e}")

    def create_day(self) -> None:
        """Create a new day's structure"""
        try:
            day_number = self.get_next_day()
            print(f"\nCreating structure for Day {day_number}...")

            self.initialize_structure(day_number)
            self.create_directories()
            self.create_solution_files()

            print(f"\nSuccessfully created Day {day_number} structure!")

        except Exception as e:
            print(f"\nError creating day structure: {e}")
            if self.structure:
                self.cleanup()
            sys.exit(1)


def main():
    creator = DayCreator()
    creator.create_day()


if __name__ == "__main__":
    main()
