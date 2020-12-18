import numpy as np

lines = []
with open('18/input', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

def combine_numbers(n1, n2, operator):
  if operator == '+':
    n1 += n2
  else:
    n1 *= n2

  return n1

def find_matching_paren(expr):
  paren_count = 0
  for i, token in enumerate(expr):
    paren_count += token.count('(') - token.count(')')

    if paren_count == 0:
      return i


def eval_expression(expr):
  num_plus = expr.count('+')
  res = 0
  operator = None
 # print(f"evaluating expression: {' '.join(expr)}")
  #input()
  res_expr = []
  while len(expr) > 0:
    token = expr.pop(0)

    if token == '(':
      group_close = find_matching_paren([token] + expr)
     # print(token, group_close)
      subexpression = ['+'] + expr[:group_close-1]
      next_val = eval_expression(subexpression)
      expr = expr[group_close:]
      #input(next_val)
      res = combine_numbers(res, next_val, '+')
      operator = None
    elif operator is not None:
      res = combine_numbers(res, int(token), operator)
      operator = None
    elif token == '+':
      operator = token
    elif token == '*':
      #print('appending', res)
      res_expr.append(res)
      res = 0
    else:
      res += int(token)

    #print(res_expr)
    #if operator is None:
     # print(f"evaluating expression: {res} {' '.join(expr)}")

  res_expr.append(res)
 # print('returning prod of', res_expr)
  return np.prod(res_expr)


def split_line(line):
  tokens = line.split(" ")

  tmp_line = ['+']

  for token in tokens:
    if '(' in token:
      pcount = token.count('(')
      tmp_line += list(token[:pcount])
      tmp_line.append(token[pcount:])
    elif ')' in token:
      pidx = token.index(')')
      tmp_line.append(token[:pidx])
      tmp_line += list(token[pidx:])
    else:
      tmp_line.append(token)

  return tmp_line


results = [0]*len(lines)
for i, line in enumerate(lines):
  tokens = split_line(line)

  results[i] = eval_expression(tokens)
  #print(f"Line: {i} gave result {results[i]}")
  #input()

print(sum(results))
