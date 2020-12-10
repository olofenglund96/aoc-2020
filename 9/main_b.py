target = 144381670
#target = 127

lines = []
with open('9/input', 'r') as file:
  lines = [int(line.strip()) for line in file.readlines()]

cont_nums = []
cont_sum = 0
for i in range(0, len(lines)):
  cont_nums.append(lines[i])
  cont_sum += lines[i]
  
  #print(cont_nums, cont_sum)
  #input()
  if cont_sum == target:
    print(min(cont_nums) + max(cont_nums))
    break
  elif cont_sum > target:
    #print('--- above target ---')
    while True:
      cont_sum -= cont_nums[0]
      del cont_nums[0]

      #print(cont_nums, cont_sum)
      if cont_sum == target:
        print(min(cont_nums) + max(cont_nums))
        exit()
      elif cont_sum < target:
        break