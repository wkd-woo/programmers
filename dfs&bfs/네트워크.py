def solution(n, computers):
    visited = [0] * len(computers)
    answer = 0
    networks = dict()
    
    def dfs(node):
        visited[node] = True
        for each in networks[node]:
            if not visited[each]:
                dfs(each)
    
    for i in range(len(computers)):
        networks[i] = []
        computers[i][i] = 0
        for j in range(i):
            if computers[i][j]:
                networks[i] += [j]
                networks[j] += [i]
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
                
    return answer