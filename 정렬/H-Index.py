def solution(citations):
    if max(citations) == 0:
        return 0

    citations.sort(reverse=True)
    h = 0
    for i, citation in enumerate(citations):
        if citation < i+1:
            return h
        else:
            h = i + 1
    return h