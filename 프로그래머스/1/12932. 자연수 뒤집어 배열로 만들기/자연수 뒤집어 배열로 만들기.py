def solution(n):
    n = str(n)
    answer = n[::-1]
    print(answer)
    answer = map(int, answer)
    answer = list(answer)
    
    return answer