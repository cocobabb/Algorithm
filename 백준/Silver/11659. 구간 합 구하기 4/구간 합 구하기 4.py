import sys
input = sys.stdin.readline
from itertools import accumulate

#  N: 수의 개수
#  M: 수들의 합을 구하는 횟수
#  i, j : 합할 수의 구간

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 누적합 배열을 미리 만들어서 해당 구간 합을 빠르게 가져온다.

# 누적합 배열 만들기1
acc_nums = [0]
for num in nums:
  acc_nums.append(acc_nums[-1]+num) 

# 누적합 배열 만들기2
# acc_nums = [0] + list(accumulate(nums))

for _ in range(M):
  i, j = map(int, input().split())

  print(acc_nums[j]-acc_nums[i-1])