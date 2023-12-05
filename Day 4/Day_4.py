import re

sum = 0

with open("input.txt") as file:
   for line in file:
      points = 0
      line.strip()
      line = re.sub(r'Card\s+\d+: ','',line.strip())
      wining_numbers = line.split(" | ")[0].split(" ")
      card_numbers = line.split(" | ")[1].split(" ")
      
      wining_numbers = [int(num) for num in wining_numbers if num]
      card_numbers = [int(num) for num in card_numbers if num]
      
 
      for number in card_numbers:
         if number in wining_numbers:
            points = points * 2 if points > 0 else 1
      sum += points

print("Sum: " + str(sum))
 