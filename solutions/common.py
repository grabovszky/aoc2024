import os


def read_input(day_number):
    # Construct the path to the input file
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    input_filename = f"day{day_number:02d}.txt"
    input_path = os.path.join(project_root, "inputs", input_filename)

    # Read the input file
    try:
        with open(input_path, "r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_path}")
