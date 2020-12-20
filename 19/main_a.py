import numpy as np

lines = []
with open('19/test', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

known_nodes = {}
unknown_nodes = {}

def parse_unknown_node(values):
  if '|' in values:
    rules = values.split(' | ')
    return [(r.split(" ")[0], r.split(" ")[1]) for r in rules]
  else:
    r1, r2 = values.split(" ")
    return [(r1, r2)]

for line in lines:
  k, v = line.split(": ")
  if line.count('"') == 2:
    known_nodes[k] = v[1:-1]
  else:
    unknown_nodes[k] = parse_unknown_node(v)

while len(unknown_nodes.keys()) > 0:
  for k, v in unknown_nodes.items():
    for rules in v:
      for rule in rules:
        if


print(known_nodes, unknown_nodes)
#for k, v in unknown_nodes.items():
