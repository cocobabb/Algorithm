from collections import Counter
    
def solution(participant, completion):
    answer = ''

    counter = Counter(participant)

    for name in completion:
        counter[name] -=1

    for name, counts in counter.items():
        if counts == 1:
            answer = name
    
    return answer