lines = []
with open('3/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

prod = 1
width = len(lines[0])
steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for step in steps:
  row = 0
  col = 0
  num_trees = 0
  while row < len(lines):
    if lines[row][col] == '#':
      num_trees += 1

    print(col, lines[row][col])
    print(lines[row])
    row += step[1]
    col = (col + step[0]) % width

  prod *= num_trees

print(prod)
