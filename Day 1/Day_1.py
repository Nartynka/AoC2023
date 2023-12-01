import re

sum = 0

dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

with open("input.txt") as file:
    for line in file:
      line = line.strip()
      num_str1 = re.search(r"(\d|one|two|three|four|five|six|seven|eight|nine)", line)[0]
      num_str2 = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)[-1]

      number = ""
      if dict.get(num_str1):
         number = dict.get(num_str1)
      else:
         number = num_str1
         
      if dict.get(num_str2):
         number += dict.get(num_str2)
      else:
         number += num_str2
      sum += int(number)

print(sum)