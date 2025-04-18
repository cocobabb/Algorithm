import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# (n-2) + (n-1) + n
max = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = nums[i] + nums[j] + nums[k]
            
            if max < total <= M:
                max = total
print(max)