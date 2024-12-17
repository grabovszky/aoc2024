from re import findall


def parse_input(input_str):
    """Parse input into initial register values and program."""
    numbers = [int(n) for n in findall(r"(\d+)", input_str)]
    return numbers[0], numbers[1], numbers[2], numbers[3:]  # a, b, c, program


class Computer:
    def __init__(self, program, a=0, b=0, c=0):
        self.program = program
        self.a = a
        self.b = b
        self.c = c
        self.ip = 0
        self.output = []

    def get_combo_value(self, operand):
        """Get value for combo operand based on registers."""
        return [0, 1, 2, 3, self.a, self.b, self.c, 99999][operand]

    def run(self):
        """Run program until halt. Returns output values."""
        while 0 <= self.ip < len(self.program):
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]
            combo = self.get_combo_value(operand)

            match opcode:
                case 0:  # adv
                    self.a = self.a // (2**combo)
                case 1:  # bxl
                    self.b = self.b ^ operand
                case 2:  # bst
                    self.b = combo % 8
                case 3:  # jnz
                    if self.a != 0:
                        self.ip = operand - 2
                case 4:  # bxc
                    self.b = self.b ^ self.c
                case 5:  # out
                    self.output.append(combo % 8)
                case 6:  # bdv
                    self.b = self.a // (2**combo)
                case 7:  # cdv
                    self.c = self.a // (2**combo)

            self.ip += 2

        return self.output
