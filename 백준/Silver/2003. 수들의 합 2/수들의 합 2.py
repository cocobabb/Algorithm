import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = list(map(int, input().split()))

i = j = 0

tmp = 0
cnt = 0

while True:
  if tmp < M:

    if j >= N:
      break
    else:
      tmp += A[j]
      j += 1

  elif tmp > M:
    tmp -= A[i]
    i += 1
  else:
    cnt += 1
    tmp -= A[i]
    i += 1

print(cnt)
  



