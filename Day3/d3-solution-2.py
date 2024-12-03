import re

with open("input.txt", "r") as file:
    lines = file.readlines()

match_results = []

# do_index_list = []
# dont_index_list = []

do_list = []

find_mul_patter = r"mul\((\d{1,3}),(\d{1,3})\)"
index =  0

result = ""
start = 0
for line in lines:
    do_index = line.find('do()')
    dont_index = line.find('don\'t()')
    
    while True:
        dont_index = line.find('don\'t()', start)
        if dont_index == -1:
            result += line[start:]
            break

        result += line[start:dont_index]
        
        do_index = line.find('do()', dont_index + 6)
        if do_index == -1:
            break

        start = do_index + 2          

    # while line.find('don\'t()') != -1:
    #     do_index = line.find('do()')
    #     dont_index = line.find('don\'t()')
    #     if do_index > dont_index:
    #         line = line[:dont_index] + line[do_index:]
    #     if dont_index > do_index:
    #         do_list.append(line[do_index:dont_index])
    #         line = line[:do_index] + line[dont_index:]    
            
    # if do_index < dont_index:   
    #     new_lines.append(line[:dont_index] + line[len(line) -1:])

    # do_index_list.append(line.find('do()'))
    # dont_index_list.append(line.find('don\'t()'))
    

    # match_list = re.findall(find_mul_patter, line)
    # for match in match_list:
    #     x, y =  map(int, match)
    #     match_results.append(x * y)

# print(sum(match_results))
print(result)