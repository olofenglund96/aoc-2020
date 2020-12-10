import networkx as nx
import matplotlib.pyplot as plt

from collections import defaultdict

lines = []
with open('10/input', 'r') as file:
  lines = [int(line.strip()) for line in file.readlines()]

lines.sort()

lines.insert(0, 0)
lines.append(lines[-1] + 3)

lines_org = lines.copy()

DG = nx.DiGraph()
nodes = defaultdict(list)

for i in range(0, len(lines)):
  for j in range(i+1, min(i+4, len(lines))):
    #print(lines[i], lines[j])

    if lines[i] + 3 >= lines[j]:
      #print(f"{lines[i]} ~> {lines[j]}")
      nodes[lines[i]].append(lines[j])
      DG.add_edge(lines[i], lines[j])

print(lines)

nodes_in_shortest_path = []

i = 0
while True:
  nodes_in_shortest_path.append(i)
  children = nodes[i]

  i = children[-1]

  if i == lines[-1]:
    break

print(nodes_in_shortest_path)

def traverse_tree(node):
  children = nodes[node]
  #print(f"{node} ~> {children}")

  if len(children) == 0:
    return 1

  if node in nodes_in_shortest_path:
    return 1
  
  childsum = 0
  for child in children:
    childsum += traverse_tree(child)
      
  #print(f"childsum: {childsum}")
  return childsum

mul = 1
while len(nodes_in_shortest_path) > 0:
  node = nodes_in_shortest_path.pop(0)
  mul *= traverse_tree(node)

print(mul)
plt.figure()
nx.draw(DG, with_labels=True, font_weight='bold')
plt.savefig("10/graph_2.png")