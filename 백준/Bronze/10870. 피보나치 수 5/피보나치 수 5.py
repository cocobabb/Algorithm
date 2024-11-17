import sys
input = sys.stdin.readline
from itertools import accumulate

n = int(input())

# 누적합 리스트 만들기
acc_nums = [0,1] 
for i in range(n+1):
  acc_nums.append(acc_nums[i]+acc_nums[-1])


print(acc_nums[n])