from collections import deque

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        cabbages[y][x] = 0
        for i, j in moves:
            if 0 <= x+i < m and 0 <= y+j < n and cabbages[y+j][x+i] == 1 and not visited[y+j][x+i]:
                queue.append((x+i, y+j))
                visited[y+j][x+i] = True

t = int(input().strip())

for _ in range(t):
    m, n, k = map(int, input().split())

    cabbages = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        cabbages[y][x] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if cabbages[i][j] == 1:
                result += 1
                bfs(j, i)

    print(result)
