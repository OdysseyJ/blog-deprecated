import sys
from collections import deque

n = int(sys.stdin.readline().strip())

for _ in range(n):
    i = int(sys.stdin.readline().strip())
    start_x, start_y = map(int, sys.stdin.readline().strip().split(" "))
    end_x, end_y = map(int, sys.stdin.readline().strip().split(" "))
    visited = [[False for _ in range(i)] for _ in range(i)]
    night_moves = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]

    queue = deque([(start_x, start_y, 0)])

    while queue:
        top_x, top_y, step = queue.popleft()
        if top_x == end_x and top_y == end_y:
            print(step)
            break
        if visited[top_y][top_x]:
            continue
        visited[top_y][top_x] = True
        for move in night_moves:
            x, y = move
            next_x = top_x+x
            next_y = top_y+y
            next_step = step+1
            if 0 <= next_x < i and 0 <= next_y < i:
                queue.append((next_x, next_y, next_step))
