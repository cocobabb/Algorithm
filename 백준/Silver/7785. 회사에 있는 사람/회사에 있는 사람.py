import sys
input = sys.stdin.readline

n = int(input())
my_dict = {}
for cnt in range(n):
  enter = (input().split())
  # 0 : 이름 / 1 : enter / leave
  my_dict[enter[0]] = enter[1]

  if my_dict[enter[0]]=='leave':
    my_dict.pop(enter[0])
    

# sorted(my_dict,reverse=True)
remain_person = list(my_dict.keys())
remain_person.sort(reverse = True)

# for idx in range(len(remain_person)):
#   print(remain_person[idx])
print(*remain_person)