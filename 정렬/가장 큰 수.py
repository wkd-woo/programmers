from functools import cmp_to_key

def comparator(a, b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) 
    
def solution(numbers):
    numbers = list(map(str, numbers))    
    numbers = sorted(numbers, key=cmp_to_key(comparator), reverse=True)
    
    if not sum(list(map(int, numbers))):
        return '0'
    return ''.join(numbers)