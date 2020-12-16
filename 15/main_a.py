import numpy as np

#seq = [7,12,1,0,16,2]
seq = [0,3,6]

n = 2020

last_indices = {v:k for k, v in enumerate(seq[:-1])}

last_num = seq[-1]
for i in range(len(seq) - 1, 30000000):
  turn = i + 1
  next_num = None
  try:
    #print(seq[i])
    turn_of_last_num = last_indices[seq[i]] + 1
    next_num = turn - turn_of_last_num
    #print(turn, turn_of_last_num)
  except KeyError:
    next_num = 0

  #print(f"Turn {turn}, Seq: {seq}, last_indices: {last_indices}")
  #input()

  seq.append(next_num)
  last_indices[last_num] = i
  last_num = next_num



  


print(seq[-2])