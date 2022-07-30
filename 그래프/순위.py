def solution(n, results):
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for winner, loser in results:
        graph[winner][loser] = 1
        graph[loser][winner] = -1

        # 플로이드-워셜 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == 1 and graph[k][j] == 1:  # i 가 k를 이기고 k가 j를 이기면
                    graph[i][j] = 1  # i는 j를 이긴다
                elif graph[i][k] == -1 and graph[k][j] == -1:  # i가 k한테 지고 k가 j한테 지면
                    graph[i][j] = -1  # i는 j한테 진다

    cnt = 0
    for i in range(1, n + 1):
        if graph[i][1:].count(0) == 1:
            cnt += 1

    return cnt
