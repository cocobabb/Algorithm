import sys
input = sys.stdin.readline
dwarfs = []
for _ in range(9):
  h = int(input())
  dwarfs.append(h)

h_total = sum(dwarfs)
fake = []
real_dwarfs =[]
out_for = False
for i in range(8):
  for j in range(i+1, 9):
    if h_total - dwarfs[i] - dwarfs[j] == 100:
      fake = [dwarfs[i], dwarfs[j]]
      out_for = True
      break
  if out_for:
    break
real_dwarfs = [el for el in dwarfs if el not in fake]
real_dwarfs.sort()

for real in real_dwarfs:
  print(real)
