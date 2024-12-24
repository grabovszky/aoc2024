import re

# Regex patterns for parsing input
INPUT_PATTERN = r"([xy]\d\d): ([10])"
GATE_PATTERN = r"([a-z0-9]{3}) ([XORAND]+) ([a-z0-9]{3}) -> ([a-z0-9]{3})"

# Bitwise operations for each gate type
OPERATIONS = {
    "XOR": lambda a, b: a ^ b,
    "OR": lambda a, b: a | b,
    "AND": lambda a, b: a & b,
}


def parse_input(content):
    """Parse input into wire values and gate operations."""
    inputs_section, gates_section = content.strip().split("\n\n")

    # Parse initial wire values (x00: 1, y00: 0, etc.)
    values = {}
    for line in inputs_section.split("\n"):
        wire, value = re.match(INPUT_PATTERN, line).groups()
        values[wire] = int(value)

    # Parse gate operations (x00 AND y00 -> z00, etc.)
    gates = []
    for line in gates_section.split("\n"):
        in1, op, in2, out = re.match(GATE_PATTERN, line).groups()
        gates.append((in1, op, in2, out))

    return values, gates


def simulate_circuit(values, gates):
    """
    Simulate the circuit by processing gates when their inputs are ready.
    Returns final values of all wires.
    """
    result = values.copy()
    operations = gates.copy()

    # Keep processing gates until all are resolved
    while operations:
        in1, op, in2, out = operations.pop(0)
        # Process gate if both inputs are ready
        if in1 in result and in2 in result:
            result[out] = OPERATIONS[op](result[in1], result[in2])
        else:
            # Put gate back in queue if inputs aren't ready
            operations.append((in1, op, in2, out))

    return result


def get_output_value(values):
    """Convert z-wire values to decimal (z00 is least significant bit)."""
    z_wires = sorted((k, v) for k, v in values.items() if k.startswith("z"))
    binary = "".join(str(v) for _, v in z_wires)
    return int(binary[::-1], 2)


def find_incorrect_wires(gates):
    """
    Find wires that are likely incorrect based on circuit patterns.
    Uses four key patterns found in RCA circuits:
    1. Z-wires should come from XOR gates (except highest bit)
    2. XOR gates should involve input/output wires
    3. AND gates should include x00 input
    4. XOR outputs shouldn't feed into OR gates
    """
    wrong_wires = set()
    # Find highest z-wire (carry bit)
    highest_z = max(
        (out for _, _, _, out in gates if out.startswith("z")), key=lambda x: int(x[1:])
    )

    for in1, op, in2, out in gates:
        # Pattern 1: Z-wires must come from XOR (except carry bit)
        if out.startswith("z") and op != "XOR" and out != highest_z:
            wrong_wires.add(out)

        # Pattern 2: XOR gates should use input/output wires
        if op == "XOR" and all(w[0] not in "xyz" for w in [out, in1, in2]):
            wrong_wires.add(out)

        # Pattern 3: AND gates should use x00 input
        if op == "AND" and "x00" not in [in1, in2]:
            for other_in1, other_op, other_in2, _ in gates:
                if out in [other_in1, other_in2] and other_op != "OR":
                    wrong_wires.add(out)

        # Pattern 4: XOR outputs shouldn't feed OR gates
        if op == "XOR":
            for other_in1, other_op, other_in2, _ in gates:
                if out in [other_in1, other_in2] and other_op == "OR":
                    wrong_wires.add(out)

    return wrong_wires
