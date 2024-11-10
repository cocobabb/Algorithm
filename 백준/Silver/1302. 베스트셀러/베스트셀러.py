from collections import Counter
N = int(input())

# 팔리는 책이름 list에 저장
sold_book = list()
for _ in range(N):
  book_name = input()
  sold_book.append(book_name)

# 집계알고리즘 이용
# 딕션너리에 key에는 책이름을 
# value에는 팔린 수가 들어가도록 함
my_dict = {}
for name in sold_book:
  if name not in my_dict:
    my_dict[name] = 1
  else:
    my_dict[name]+=1

# 정렬함수 이용하여 정렬할 때 lambda함수를 이용해 기준을 무엇으로 정렬할 건지 정함
# dictionary.items() >>(key,value)형태로 list를 생성함 
sorted_my_dict = sorted(my_dict.items(),key = lambda x : (-x[1],x[0]))
print(sorted_my_dict[0][0])




