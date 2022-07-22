def solution(prices):
    stack = []
    # 해당 시점으로부터 시간이 얼마나 지났는 지
    answer = [len(prices) - i - 1 for i in range(len(prices))]
    for i, price in enumerate(prices):
        if not stack: # 스택이 비었으면 추가
            stack.append((i, price))
            
        else:
            while stack and price < stack[-1][1]: # 스택이 있을때 현재 가격이 스택 맨 위 가격보다 낮을 때마다
                answer[stack[-1][0]] -= 1 # 가격이 떨어진 초 만큼 뺌
                stack.pop() # 스택 pop()
            stack.append((i, price))

    return answer

ins = list(map(int, input().split()))
print(solution(ins))