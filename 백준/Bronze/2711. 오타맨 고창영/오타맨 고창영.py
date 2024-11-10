T = int(input())

for t in range(T):
  idx, word = input().split(' ')
  idx = int(idx)
  
  print(word[:idx-1] + word[idx:])