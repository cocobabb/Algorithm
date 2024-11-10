import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  total = 0
  cnt = 0
  case = input()
  for el in case:
    if el=='O':
      cnt+=1
      total+=cnt
    elif el=='X':
      cnt=0
  print(total)