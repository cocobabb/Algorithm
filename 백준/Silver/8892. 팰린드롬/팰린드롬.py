
import sys
input = sys.stdin.readline
from itertools import combinations,permutations

T = int(input())

for _ in range(T):
  words = []
  k = int(input())
  for _ in range(k):
    word = input().strip("\n")
    words.append(word)
  
  for w in permutations(words,2):
    w1, w2 = w
    palindrome = w1+w2
    if palindrome == palindrome[::-1]:
      print(palindrome)
      break
  else:
    print(0)
