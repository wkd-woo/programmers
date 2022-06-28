import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2 and scoville[0] < K:        
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        mixed = one + two * 2
        heapq.heappush(scoville, mixed)
        answer += 1
    
    if scoville[0] < K:
        return -1
        
    return answer