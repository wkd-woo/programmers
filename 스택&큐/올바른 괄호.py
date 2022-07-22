def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack += [c]
        elif not stack:
            return False
        else:
            stack.pop()
    
    if stack:
        return False
    
    return True