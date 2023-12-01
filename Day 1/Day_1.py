import re

sum = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        number1 = re.search("\d", line)[0]
        number2 = re.findall("\d", line)[-1]
        sum += int(number1 + number2)

print(sum)
