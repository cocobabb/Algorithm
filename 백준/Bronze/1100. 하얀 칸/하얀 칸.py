matrix = [list(input()) for _ in range(8)]
count = 0
checkWhite = False
for i in range(8):
    for j in range(8):
        # 행이 짝수이고 열이 짝수면 하얀칸
        # 행이 홀수이고 열이 홀수면 하얀칸
        if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
           checkWhite = True
        if checkWhite and matrix[i][j] == 'F': 
            count+=1
        checkWhite = False
print(count)