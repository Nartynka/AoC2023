file = open("input.txt")
lines = file.read().splitlines()
# Grid contains columns
grid = list(map("".join, zip(*lines)))
new_grid = []
# row in grid is a column in the input
for row in grid:
   groups = row.split("#")
   new_column = []
   for group in row.split("#"):
      a = sorted(list(group), reverse=True)
      new_column.append("".join(a))
   new_column = "#".join(new_column)
   new_grid.append(new_column)
new_grid = list(map("".join, zip(*new_grid)))

sum = 0
for i, row in enumerate(new_grid):
   sum+= row.count("O")*(len(new_grid)-i)

print(sum)