with open("input.txt", "r") as file:
    lines = file.readlines()

safe = []

def check_safety(list):
    all_increase_with_adjacent_check = all(1 <= (list[i + 1] - list[i]) <= 3 for i in range(len(list) - 1))

    all_decrease_with_adjacent_check = all(1 <= (list[i] - list[i + 1]) <= 3  for i in range(len(list) - 1))

    return all_increase_with_adjacent_check or all_decrease_with_adjacent_check

for line in lines:
    list_from_line = [int(num) for num in line.split()]
    if check_safety(list_from_line):
        safe.append(list_from_line)

print(len(safe))