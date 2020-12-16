import numpy as np
import itertools

lines = []
with open('14/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

memory = {}
curr_mask = ""

for i, line in enumerate(lines):
  inf, val = line.split(" = ")

  if inf == "mask":
    curr_mask = val
    #print(curr_mask)
  else:
    address = inf[4:-1]
    binary_number = "{0:036b}".format(int(address))
    #print(len(binary_number), len(curr_mask))

    new_binary_number = []
    for i in range(0, len(binary_number)):
      #print(binary_number, i, binary_number[i])
      if curr_mask[i] != '0':
        new_binary_number.append(curr_mask[i])
      else:
        new_binary_number.append(binary_number[i])

    x_index = [i for i, x in enumerate(new_binary_number) if x == "X"]
    x_index.reverse()

    combinations = ["".join(seq) for seq in itertools.product("01", repeat=len(x_index))]

    for binary_num in combinations:
      #print(i, binary_num)
      tbn = new_binary_number.copy()
      for j, idx in enumerate(x_index):
        #print(idx, tbn[idx], binary_num[len(binary_num) - 1 - j])
        tbn[idx] = binary_num[len(binary_num) - 1 - j]
      
      tbn = "".join(tbn)
      #print(binary_num, tbn, int(tbn, 2))
      memory[tbn] = int(val)

    #print(address, int(new_binary_number, 2), binary_number, new_binary_number)
    #input()

#print(memory)

print(sum(memory.values()))