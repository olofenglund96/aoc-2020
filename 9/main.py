window = 25

lines = []
with open('9/input', 'r') as file:
  lines = [int(line.strip()) for line in file.readlines()]

for i in range(window, len(lines)):
  valid_nums = []

  for n1 in lines[i-window:i]:
    for n2 in lines[i-window:i]:
      valid_nums.append(n1 + n2)

  valid_nums = set(valid_nums)

  if lines[i] not in valid_nums:
    print(lines[i])
    break