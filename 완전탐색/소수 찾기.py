from itertools import permutations
import math

# 소수 판별
def isPrime(x):
    if x in (0, 1):
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True
                    

def solution(numbers):
    suspect = set()
    
    for i in range(1, len(numbers) + 1):
        for each in permutations(numbers, i):
            temp = int(''.join(each))
            if isPrime(temp):
                suspect.add(temp)
                    
    return len(suspect)