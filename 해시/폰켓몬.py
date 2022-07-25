def solution(nums):
    table = {}
    for num in nums:
        if num not in table:
            table[num] = 0
        table[num] += 1

    target = list(table.keys())
    if len(target) < len(nums)//2:
        return len(target)

    return len(nums)//2
