import sys
from collections import deque

n, m, = map(int, sys.stdin.readline().strip().split(" "))
nodes = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().strip().split(" "))
    nodes[n1][n2] = 1
    nodes[n2][n1] = 1

def g_bfs(start_node):
    queue = deque([start_node])
    result = []
    while queue:
        top = queue.popleft()
        if visited[top]:
            continue

        result.append(str(top))
        visited[top] = True

        for idx, linked in enumerate(nodes[top][1:]):
            if linked == 1 and not visited[idx+1]:
                queue.append(idx+1)

    return result

result = 0
for i in range(1, n+1):
    if len(g_bfs(i)) != 0:
        result += 1

print(result)
