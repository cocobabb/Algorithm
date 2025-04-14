import sys
input = sys.stdin.readline

N = input()
originNumbers = map(int, input().split())

numbers = {}

for key in originNumbers:
    if key in numbers:
        numbers[key] += 1
    else:
        numbers[key] = 1

M = input()
comparedNumbers = map(int, input().split())

for key in comparedNumbers:
    if key in numbers:
        print(numbers[key], end=" ")
    else:
        print(0,end=" ")