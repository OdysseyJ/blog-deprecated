import sys
from collections import deque


def find_edges(islands, x, y, w, h):
    results = []
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if 0 <= i < h and 0 <= j < w:
                if i == y and j == x:
                    continue
                if islands[i][j] == "1":
                    results.append((w*y+x, w*i+j))
    return results


while True:
    w, h = map(int, sys.stdin.readline().strip().split(" "))
    if w == 0 and h == 0:
        break
    n = w * h
    nodes = [[0 for _ in range(n)] for _ in range(n)]
    islands = [input().split(" ") for _ in range(h)]
    visited = [False for _ in range(n)]

    for y in range(h):
        for x in range(w):
            if islands[y][x] == "1":
                edges = find_edges(islands, x, y, w, h)
                for edge in edges:
                    n1, n2 = edge
                    nodes[n1][n2] = 1
            else:
                visited[w*y+x] = True

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
    for i in range(n):
        r = g_bfs(i)
        if len(r) != 0:
            result += 1

    print(result)
