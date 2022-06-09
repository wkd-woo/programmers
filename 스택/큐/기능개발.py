import math

def solution(progresses, speeds):
    answer = []
    stack = []
    for progress, speed in zip(progresses, speeds):
        mp = math.ceil((100 - progress)/speed)
        if not stack:
            stack = [mp]
        elif mp <= max(stack):
            stack += [mp]
        else:
            answer += [len(stack)]
            stack = [mp]
        
    return answer + [len(stack)]