import re

sum = 0

with open("input.txt") as file:
   for line in file:
      game_id = int(line.split(":")[0].split("Game")[1])
      line = line.strip().split(":")[1]

      games = line.split(";")

      min_red = 0
      min_green = 0
      min_blue = 0

      for game in games:
         red_cubes = 0
         green_cubes = 0
         blue_cubes = 0

         red_str = re.search(r"\d+ red", game)
         if red_str:
            red_cubes = int(red_str[0].strip(" red"))

         green_str = re.search(r"\d+ green", game)
         if green_str:
            green_cubes = int(green_str[0].strip(" green"))

         blue_str = re.search(r"\d+ blue", game)
         if blue_str:
            blue_cubes = int(blue_str[0].strip(" blue"))
         
         if red_cubes > min_red:
            min_red = red_cubes

         if green_cubes > min_green:
            min_green = green_cubes

         if blue_cubes > min_blue:
            min_blue = blue_cubes

      sum += min_red*min_green*min_blue

print(sum)
            
