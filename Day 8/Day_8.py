from math import gcd

directions, _, *rest = open("input.txt").read().splitlines()
sum = 0

# key: [left, right]
network = {}

for line in rest:
   pos, targets = line.split(" = ")
   # Remove parentheses and split
   network[pos] = targets[1:-1].split(", ")

start_positions = [pos for pos in network if pos.endswith("A")]
cycles = []

for current in start_positions:
   cycle = []

   dir_idx = 0
   steps_count = 0
   first_z = None
   while True:
      while steps_count == 0 or not current.endswith("Z"):
         steps_count += 1
         if directions[dir_idx] == "L":
            current = network[current][0]
         else:
            current = network[current][1]
         dir_idx+=1
         if dir_idx >= len(directions):
            dir_idx = 0
      cycle.append(steps_count)
      if first_z is None:
         first_z = current
         steps_count = 0
      elif first_z == current:
         break

   cycles.append(cycle)

# Add only first element from each cycle
nums = [cycle[0] for cycle in cycles]

NWW = nums.pop() 

for num in nums:
   # // divides and then rounds down :pog:
   # LCM = NWW, GCD = NWD
   NWW = (NWW * num) // gcd(NWW, num)

print(NWW)