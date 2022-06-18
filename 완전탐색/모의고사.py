def solution(answers):
    result = []
    
    one = [1, 2, 3, 4, 5] * 10000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 10000
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000
    
    score_one = 0
    score_two = 0
    score_three = 0
    
    for mark, answer in zip(one, answers):
        if mark == answer:
            score_one += 1
    for mark, answer in zip(two, answers):
        if mark == answer:
            score_two += 1
    for mark, answer in zip(three, answers):
        if mark == answer:
            score_three += 1
            
    mx = max(score_one, score_two, score_three)
    
    if mx == score_one:
        result += [1]
    if mx == score_two:
        result += [2]
    if mx == score_three:
        result += [3]
    
    return sorted(result)