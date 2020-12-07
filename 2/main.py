lines = []
with open('2/input', 'r') as file:
  lines = file.readlines()

limits = [[int(lim)-1 for lim in line.split(" ")[0].split("-")] for line in lines]
chars = [line.split(" ")[1][0] for line in lines]
passwords = [line.split(" ")[2] for line in lines]

valid_passwords = 0
for i in range(0, len(lines)):
  low, up = limits[i]
  char = chars[i]
  passw = passwords[i]

  if (passw[low] == char and passw[up] != char) or (passw[low] != char and passw[up] == char):
    valid_passwords += 1

print(valid_passwords)
