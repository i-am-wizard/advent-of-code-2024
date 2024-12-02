with open("input.txt", "r") as file:
    lines = file.readlines()

list1 = []
list2 = []

for line in lines:
    numbers = line.strip().split("   ")
    list1.append(int(numbers[0]))
    list2.append(int(numbers[1]))

list1.sort()
list2.sort()

differences = [abs(a - b) for a, b in zip(list1, list2)]
total_diff = sum(differences)

print(total_diff)