# N: 온도를 측정한 전체 날짜의 수 
# K: 구간합을 구하기 위한 연속적인 날짜의 수
N, K = map(int, input().split())
daily_check = list(map(int, input().split()))

tmp = sum(daily_check[:K])
max_sum = tmp

for idx in range(N-K):
  tmp += daily_check[idx+K] - daily_check[idx]
  max_sum = max(max_sum,tmp)
print(max_sum)