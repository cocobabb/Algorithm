low = ['a', 'e', 'i', 'o', 'u']
upper = ['A', 'E', 'I', 'O', 'U']

sum = 0
# #이 나오기 전까지 입력 받기기
while True:
    sentence = input()
    if sentence == '#':
        break
    # 입력 받은 문장의 모음 수 세기
    for w in sentence:
        if w in low or w in upper:
            sum+=1
    print(sum)
    sum = 0