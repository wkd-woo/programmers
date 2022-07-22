def solution(s):
    answer = []
    for c in s:
        if not answer or answer[-1] != c:
            answer += [c]
        elif answer[-1] == c:
            continue
    return answer