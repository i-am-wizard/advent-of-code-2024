import re

with open("input.txt", "r") as file:
    lines = file.readlines()

match_results = []

find_mul_patter = r"mul\((\d{1,3}),(\d{1,3})\)"

for line in lines:
    match_list = re.findall(find_mul_patter, line)
    for match in match_list:
        x, y =  map(int, match)
        match_results.append(x * y)

print(sum(match_results))