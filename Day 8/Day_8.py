import re, sys
sys.setrecursionlimit(25000)
sum = 0

file = open("input.txt")
directions = file.readline().strip()
file.readline()
lines = file.readlines()

str_to_search = "AAA"

dir_idx = 0

def find_next_direction():
   global str_to_search, dir_idx, sum
   for line in lines:
      line = line.strip()
      if re.search("^"+str_to_search, line):
         line = line.split(" = ")[1]
         left, right = line.strip("(").strip(")").split(", ")
         if directions[dir_idx] == "L":
            str_to_search = left
         elif directions[dir_idx] == "R":
            str_to_search = right
         if dir_idx >= len(directions)-1:
            dir_idx = 0
         else:
            dir_idx+=1
         sum+=1
         if str_to_search != "ZZZ":
            find_next_direction()
         break

find_next_direction()
print("Steps:", sum)


