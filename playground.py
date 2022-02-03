import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

def dfs(node, cnt):
    global result

    visited[node] = True
    if cnt == 5:
        result = 1

    for i in nodes[node]:
        if not visited[i]:
            dfs(i, cnt+1)
            visited[i] = False
            if result:
                return

n, m = map(int, input().strip().split(" "))
nodes = [[] for _ in range(n)]
visited = [False for _ in range(n)]
result = 0

for i in range(m):
    n1, n2 = map(int, input().strip().split(" "))
    nodes[n1].append(n2)
    nodes[n2].append(n1)

for i in range(n):
    if not visited[i]:
        dfs(i, 1)
        visited[i] = False
        if result:
            break

print(result)
