def dfs(node, target, cnt):
    visited[node] = True
    if target in dic[node]:
        return cnt + 1
    for each in dic[node]:
        if not visited[each]:
            return dfs(each, target, cnt + 1)
        

def solution(begin, target, words):
    global visited, dic, answer
    answer, dic, visited = 0, {}, {}

    if not target in words:
        return answer

    words += [begin]
    for word in words:
        visited[word] = False
        dic[word] = set()
        
    for word in words:
        for key in dic.keys():
            std = 0
            for one, two in zip(word, key):
                if one != two:
                    std += 1
            if std == 1: # 차이가 한개씩 나면 value list에 추가함.
                dic[word].add(key)
                dic[key].add(word)
    
    answer = dfs(begin, target, 0)
    
    return answer