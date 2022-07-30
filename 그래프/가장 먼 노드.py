import heapq


def dijkstra(graph, start):  # 그래프 정보와 출발노드를 받아야 함
    distances = {node: int(1e9) for node in graph}  # 거리 정보 설정
    distances[start] = 0  # 출발점 거리는 0
    queue = []
    # 우선순위 queue를 초기화 함. 출발점 거리(0)와 출발 노드
    heapq.heappush(queue, [distances[start], start])

    while queue:  # queue에 노드가 있으면
        curr_distance, curr_node = heapq.heappop(
            queue)  # 우선순위가 가장 높은 것(거리가 가장 짧은 노드) 을 pop()

        if distances[curr_node] < curr_distance:  # 저장된 거리 정보가 지금 거리보다 짧다면
            continue  # skip

        # queue에서 뽑은 node 연결 정보 확인
        for adjacent, weight in graph[curr_node].items():
            distance = curr_distance + weight  # 뽑은 node 까지 온 거리와 연결된 node의 거리를 더해 계산함

            if distance < distances[adjacent]:  # 계산한 거리가 저장된 거리 정보보다 짧다면
                distances[adjacent] = distance  # 거리 정보 갱신하고
                heapq.heappush(queue, [distance, adjacent])  # 우선순위 큐에 넣음

    return distances  # 거리 정보를 반환


def solution(n, edge):
    INF = int(1e9)
    graph = dict()
    for node1, node2 in edge:
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        graph[node1][node2] = 1
        graph[node2][node1] = 1

    temp = dijkstra(graph, 1)
    target = max(temp.values())
    return list(temp.values()).count(target)
