import sys
input = sys.stdin.readline

# n개의 수들 중
n = int(input())
num_list = list(map(int,input().split()))
# 두 수의 합이 x을 만족하는 두 수 찾기
x = int(input()) 

i = 0
j = n - 1
cnt = 0
tmp = 0
# 리스트 정렬하여 규칙성을 주고 두 포인터를 양쪽에 배치해 이용
num_list.sort()


while i < j:
  tmp = num_list[i]+num_list[j]
  # 임시 합이 x보다 작을 때
  if tmp < x:
    i+=1
        
  # 임시 합이 x랑 같을 때
  elif tmp == x:
    cnt+=1
    j-=1

  # 임시 합이 x보다 클 때
  else:
   j-=1


print(cnt)