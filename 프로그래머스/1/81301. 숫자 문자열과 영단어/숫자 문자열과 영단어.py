def solution(s):
    answer = 0
    changeNum = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
    
    for idx, value in enumerate(changeNum):
        s = s.replace(value, str(idx))
    answer = int(s)
    return answer