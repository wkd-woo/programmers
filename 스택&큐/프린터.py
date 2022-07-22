from queue import deque

def solution(priorities, location):
    answer = 0
    idx = deque(0 for i in range(len(priorities)))
    idx[location] = 1
    que = deque(priorities)
    
    while que:
        if que[0] == max(que):
            answer += 1
            if idx[0]:
                return answer
            que.popleft()
            idx.popleft()
        else:
            que.append(que.popleft())
            idx.append(idx.popleft())