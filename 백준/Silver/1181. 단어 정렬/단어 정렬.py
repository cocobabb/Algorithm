import sys

input = sys.stdin.readline

# N: 단어의 개수
# 길이가 짧은 것부터
# 길이가 같으면 사전 순
# 으로 정렬
# 단, 중복된 단어는 하나만 남기고 제거
N = int(input())
words = []
for _ in range(N):
    word = input().rstrip()
    words.append(word)

# 중복값 제거
words = list(set(words))
# sorted: 반복 가능한(iterable) 객체를 오름차순으로 정렬된 리스트로 반환
# .sort: 리스트를 오름차순으로 정렬
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
