from itertools import combinations

def solution(clothes):
    dic = {}
    answer = 1
    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]] = [cloth[0]]
        else:
            dic[cloth[1]].append(cloth[0])
    
    for key, value in dic.items():
        answer *= (len(list(combinations(value, 1))) + 1)
        
    return answer - 1 # 전부 다 선택 안할 경우 뺌