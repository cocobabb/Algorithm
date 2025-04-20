def solution(nums):
    answer = 0
    count_choice = len(nums) // 2

    category = set(nums)
    count_category = len(category)

    if count_choice > count_category:
        answer = count_category
    else:
        answer = count_choice
    
    return answer