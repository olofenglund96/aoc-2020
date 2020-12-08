from collections import defaultdict

instring = 'shiny gold'
constr = 'contain'
lines = []
with open('7/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

nodes = defaultdict()

for line in lines:
  bag_idx = line.find('bags')
  parent = line[:bag_idx].strip()

  contain_idx = line.find(constr)

  child_bag_str = line[contain_idx+len(constr)+1:]

  cb_words = child_bag_str.split(" ")

  child_bags = []

  i = 0
  if cb_words[0] != 'no':
    while i < len(cb_words):
      num = int(cb_words[i])
      bag_type = " ".join(cb_words[i+1:i+3])
      for j in range(0, num):
        child_bags.append(bag_type)
      
      i += 4
  
  nodes[parent] = child_bags

print(nodes)
bags_with_gold = {k: 0 for k in nodes.keys()}
visited = []

def bfs(parent, children):
  print(f"{parent} -> {children}")
  print(f"Visited: {visited}")
  if instring in children:
    bags_with_gold[parent] = 1
    return True
  else:
    for child in children:
      if child not in visited:
        visited.append(child)
        if bfs(child, nodes[child]):
          #input(f"{parent} has gold")
          bags_with_gold[parent] = 1
          return True
      else:
        if bags_with_gold[child] == 1:
          bags_with_gold[parent] = 1
          return True
  return False

def bfs2(parent, children):
  bagsum = 1

  for child in children:
    bagsum += bfs2(child, nodes[child])
  
  return bagsum

tot_count = bfs2(instring, nodes[instring])

print(tot_count-1)