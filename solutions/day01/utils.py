def parse_input(content):
    left_list = []
    right_list = []

    for line in content.strip().splitlines():
        numbers = line.strip().split()
        if len(numbers) >= 2:
            left_num, right_num = int(numbers[0]), int(numbers[1])
            left_list.append(left_num)
            right_list.append(right_num)
    return left_list, right_list
