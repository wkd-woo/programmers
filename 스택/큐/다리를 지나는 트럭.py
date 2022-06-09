from queue import deque

def tick_tock(x):
    return x + 1


def solution(bridge_length, weight, truck_weights):
    answer = 0
    que, bridge, bridge_t = deque(truck_weights), deque(), deque()

    while que:
        answer += 1
        bridge_t = deque(map(tick_tock, bridge_t))
        
        if bridge_t:
            if bridge_t[0] == bridge_length:
                bridge_t.popleft()
                bridge.popleft()
            
        if (len(bridge) < bridge_length) and (sum(bridge) + que[0] <= weight):
            bridge.append(que.popleft())
            bridge_t.append(0)
        
    return answer + bridge_length