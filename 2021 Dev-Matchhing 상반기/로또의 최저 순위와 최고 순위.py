def solution(lottos, win_nums):
    corr, abstract = 0, 0
    abstract = lottos.count(0)
    for num in lottos:
        if num in win_nums:
            corr += 1

    mn = 6 if corr < 2 else 7 - corr
    mx = 6 if (corr + abstract) < 2 else 7 - (corr + abstract)
    return [mx, mn]
