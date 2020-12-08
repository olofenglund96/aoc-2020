from collections import Counter

lines = []
with open('6/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

count = 0
bufstr = ""
line_no = 0
for line in lines:
  if line == "":
    c = Counter(bufstr)
    for v in c.values():
      if v == line_no:
        count += 1
    
    line_no = 0
    bufstr = ""
    continue
  
  bufstr += line
  line_no += 1

c = Counter(bufstr)
for v in c.values():
  if v == line_no:
    count += 1
print(count)