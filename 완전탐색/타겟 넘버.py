from itertools import product

pm = [1, -1]

def solution(numbers, target):
    answer = 0
    
    for i in list(product(pm, repeat=len(numbers))):
        temp = 0 
        for number, opt in zip(numbers, i):
            temp += (number * opt)
        if temp == target:
            answer += 1
            
    return answer