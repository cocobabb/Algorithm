h, m = map(int,input().split())
m = m-45
if m < 0:
    h = h-1
    m = m+60
if h < 0:
    h = h +24
    
print(h, end=' ')
print(m)