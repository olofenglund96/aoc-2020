import numpy as np

lines = []
with open('14/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

memory = {}
curr_mask = ""

for line in lines:
  inf, val = line.split(" = ")

  if inf == "mask":
    curr_mask = val
    print(curr_mask)
  else:
    binary_number = "{0:036b}".format(int(val))
    address = inf[4:-1]
    #print(len(binary_number), len(curr_mask))

    new_binary_number = []
    for i in range(0, len(binary_number)):
      #print(binary_number, i, binary_number[i])
      if curr_mask[i] != 'X':
        new_binary_number.append(curr_mask[i])
      else:
        new_binary_number.append(binary_number[i],)
    
    new_binary_number = "".join(new_binary_number)
    memory[address] = int(new_binary_number, 2)

    #print(address, int(new_binary_number, 2), binary_number, new_binary_number)
    #input()


print(sum(memory.values()))



