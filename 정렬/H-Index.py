def solution(citations):
    if max(citations) == 0:
        return 0

    citations.sort(reverse=True)
    for i in range(len(citations)):
        if i >= citations[i]:
            return i