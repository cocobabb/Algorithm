# 1. 자주 나오면
# 2. 단어 길이가 길면
# 3. 사전 순
# 앞에 배치
import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
words = [input().rstrip() for _ in range(n)]

counter = Counter(words)
unique_words = counter.keys()
# sorted 기본 값 오름차순
# 값을 음수로 바꿔주면 내림차순 효과를 낼 수 있음
# "lambda 매개변수: 리턴값(조건1, 조건2 ...)" =>  앞에 있는 조건이 더 우선순위
result = sorted(unique_words, key=lambda x: (-counter[x], -len(x), x))

# 특정 길이 이상의 단어만 암기
for word in result:
    if len(word) >= m:
        print(word)
