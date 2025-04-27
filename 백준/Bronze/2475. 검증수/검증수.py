numbers = map(int, input().split())
a = 0
for x in numbers:
    a = a + (x*x)
a = a%10
print(a)