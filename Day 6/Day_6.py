file = open("input.txt")

time = int(file.readline().strip("Time: ").replace(" ", ""))
max_distance = int(file.readline().strip("Distance: ").replace(" ", ""))

num_of_ways = 0

for i in range(1, time-1):
   speed = 0
   distance = 0
   hold_time = i

   speed += hold_time
   travel_time = time - hold_time

   distance += speed * travel_time
   
   if distance > max_distance:
      num_of_ways+=1

print(num_of_ways)