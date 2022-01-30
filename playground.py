import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(" "))

maze = [[i for i in input()] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def can_move(x, y, n, m):
    if 0 <= x < m and 0 <= y < n:
        if visited[y][x]:
            return False
        if maze[y][x] == "1":
            return True
    return False

queue = deque([(0, 0, 1)])
while queue:
    x, y, step = queue.popleft()
    if x==m-1 and y==n-1:
        print(step)
        break
    if can_move(x+1, y, n, m):
        queue.append((x+1, y, step+1))
        visited[y][x+1] = True
    if can_move(x-1, y, n, m):
        queue.append((x-1, y, step+1))
        visited[y][x-1] = True
    if can_move(x, y+1, n, m):
        queue.append((x, y+1, step+1))
        visited[y+1][x] = True
    if can_move(x, y-1, n, m):
        queue.append((x, y-1, step+1))
        visited[y-1][x] = True
