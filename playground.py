import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().strip().split(" "))
maze = [[0 for _ in range(m+1)] for _ in range(n+1)]
visited = [[False for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    line = input().strip()
    for j, c in enumerate(line):
        maze[i][j+1] = int(c)

def is_valid(x, y):
    if 1 <= x <= m and 1 <= y <= n:
        return True
    return False

def bfs():
    queue = deque([(1, 1, 0)])

    while queue:
        x, y, score = queue.popleft()

        if x == m and y == n:
            print(score)
            return

        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if is_valid(x+i, y+j) and not visited[y+j][x+i]:
                if maze[y+j][x+i] == 0:
                    queue.appendleft((x+i, y+j, score))
                    visited[y+j][x+i] = True
                else:
                    queue.append((x+i, y+j, score+1))
                    visited[y+j][x+i] = True

bfs()
