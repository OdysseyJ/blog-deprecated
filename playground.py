import sys
from collections import deque

m, n = map(int, sys.stdin.readline().strip().split(" "))

origin_tomatoes = 0
empty = 0
queue = deque([])
visited = [[False for _ in range(m)] for _ in range(n)]

for y in range(n):
    tomatoes = sys.stdin.readline().strip().split(" ")
    for x, t in enumerate(tomatoes):
        if t == "0":
            origin_tomatoes += 1
        if t == "1":
            queue.append((x, y))
            visited[y][x] = True
        if t == "-1":
            empty += 1
            visited[y][x] = True

changed = len(queue)
step = 0
is_invalid = False
if m*n == origin_tomatoes + empty:
    print(-1)
else:
    while queue:
        new_queue = deque([])
        while queue:
            x, y = queue.pop()
            if 0 <= x-1 < m and 0 <= y < n and not visited[y][x-1]:
                visited[y][x-1] = True
                new_queue.append((x-1, y))
            if 0 <= x+1 < m and 0 <= y < n and not visited[y][x+1]:
                visited[y][x+1] = True
                new_queue.append((x+1, y))
            if 0 <= x < m and 0 <= y-1 < n and not visited[y-1][x]:
                visited[y-1][x] = True
                new_queue.append((x, y-1))
            if 0 <= x < m and 0 <= y+1 < n and not visited[y+1][x]:
                visited[y+1][x] = True
                new_queue.append((x, y+1))
        if len(new_queue) == 0:
            if changed + empty != m * n:
                is_invalid=True
        else:
            changed += len(new_queue)
            step += 1
        queue = new_queue

    if is_invalid:
        print(-1)
    else:
        print(step)
