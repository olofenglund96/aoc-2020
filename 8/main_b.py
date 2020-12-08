import networkx as nx
import matplotlib.pyplot as plt

lines = []
with open('8/test2', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

instructions = []
for line in lines:
  op, num = line.split(' ')

  instructions.append((op, int(num)))

def perform_instruction(op, num):
  if op == 'acc':
    return 1
  elif op == 'jmp':
    return num
  else:
    return 1

DG = nx.DiGraph()

for i, instr in enumerate(instructions):
  op, num = instr
  j = i + perform_instruction(op, num)
  DG.add_edge(i+1, j+1)

plt.figure()
nx.draw(DG, with_labels=True, font_weight='bold')
plt.savefig("graph2.png")
