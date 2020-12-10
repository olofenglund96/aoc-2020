lines = []
with open('10/input', 'r') as file:
  lines = [int(line.strip()) for line in file.readlines()]

lines.sort()

lines.insert(0, 0)

print(lines)

diff_1 = 0
diff_3 = 0

for i in range(0, len(lines)-1):
  if lines[i+1] - lines[i] == 1:
    diff_1 += 1
  elif lines[i+1] - lines[i] == 3:
    diff_3 += 1

print(diff_1, diff_3 + 1)

print(diff_1 * (diff_3 + 1))
