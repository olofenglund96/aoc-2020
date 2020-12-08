lines = []
with open('8/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

instructions_org = []
for line in lines:
  op, num = line.split(' ')

  instructions_org.append((op, int(num)))

def perform_instruction(op, num, acc):
  if op == 'acc':
    acc += num
    return 1, acc
  elif op == 'jmp':
    return num, acc
  else:
    return 1, acc

changed = [False]*len(instructions_org)
instructions = instructions_org.copy()
while True:
  acc = 0
  visited = [False]*len(instructions)
  i_counter = 0
  last_nop_or_jmp = -1

  while True:
    #print(i_counter)
    visited[i_counter] = True
    op, num = instructions[i_counter]
    if (op == 'jmp' or op == 'nop') and not changed[i_counter]:
      last_nop_or_jmp = i_counter
    
    #print(f"line: {i_counter}, op: {op} {num}")
    #input()
    i_change, acc = perform_instruction(op, num, acc)
    i_counter += i_change

    if i_counter >= len(instructions):
      print(acc)
      exit()

    if visited[i_counter]:
      oper, num = instructions[last_nop_or_jmp]
      instructions = instructions_org.copy()
      #print("--- next node is visited ---")
      #print(f"line: {i_counter}, op: {oper} {num}")
      if oper == 'nop':
        instructions[last_nop_or_jmp] = ("jmp", num)
      else:
        instructions[last_nop_or_jmp] = ("nop", num)

      changed[last_nop_or_jmp] = True
      break
    


    #print(op, num, acc)