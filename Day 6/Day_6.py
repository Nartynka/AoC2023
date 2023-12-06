import re

sum = 1

file = open("input.txt")

times = file.readline().strip("Time: ").split("     ")
max_distances = file.readline().strip("Distance: ").split("  ")

times = [int(num) for num in times]
max_distances = [int(num) for num in max_distances]

for idx, time in enumerate(times):
   num_of_ways = 0
   for i in range(1, time-1):
      speed = 0
      distance = 0
      hold_time = i

      speed += hold_time
      travel_time = time - hold_time

      while travel_time > 0:
         distance+=speed
         travel_time-=1
      if distance > max_distances[idx]:
         num_of_ways+=1
   sum*=num_of_ways

print("Sum: ", sum)