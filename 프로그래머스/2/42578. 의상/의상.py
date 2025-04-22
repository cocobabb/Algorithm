from collections import Counter

def solution(clothes):
    answer = 0
    cloth_types = [cloth_type for c, cloth_type in clothes]
    counter = Counter(cloth_types)
    print(counter)

    answer = 1
    for counts in counter.values():
        # +1은 해당 아이템을 안입는 경우의 수를 추가한 것 
        answer *= counts + 1 

    # 현재 answer에는 각 아이템을 안입는 경우의 수들도 추가된 상태
    # 아무 아이템도 착용하지 않는 경우 1개를 제외하기 위해 -1
    answer -= 1
    return answer