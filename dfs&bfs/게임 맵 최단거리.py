from collections import deque


def solution(maps):
    # 좌표평면 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    r, c = len(maps), len(maps[0])

    q = deque()
    q.append((0, 0))

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= c or ny < 0 or ny >= r:
                continue

            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                q.append((ny, nx))

    return -1 if maps[-1][-1] == 1 else maps[-1][-1]
