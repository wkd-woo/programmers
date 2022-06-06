def solution(participant, completion):
    marthoner = dict()
    for person in participant:
        if person in marthoner:
            marthoner[person] += 1
        else:
            marthoner[person] = 1
    
    for person in completion:
        marthoner[person] -= 1
    
    for key, value in marthoner.items():
        if value == 1:
            return key 
    