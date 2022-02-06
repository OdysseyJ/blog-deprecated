import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input().strip())
edges = [map(int, input().strip().split(" ")) for _ in range(n)]
nodes = [[] for _ in range(n+1)]

for edge in edges:
    n1, n2 = edge
    nodes[n1].append(n2)
    nodes[n2].append(n1)

def find_circular_nodes(start, history, visited):
    global circular_nodes
    visited[start] = True
    new_history = history + [start]

    for node in nodes[start]:
        if visited[node] and history and node != history[-1]:
            circular_nodes = [i for i in new_history[new_history.index(node):]]
            break
        if not visited[node]:
            find_circular_nodes(node, new_history, visited)
            visited[node] = False



def bfs(start, visited):
    queue = deque([(start, 0)])
    while queue:
        top, depth = queue.popleft()
        visited[top] = depth

        for e in nodes[top]:
            if visited[e] == -1:
                queue.append((e, depth+1))
                visited[e] = depth+1

visited = [False for _ in range(n+1)]
circular_nodes = []
find_circular_nodes(1, [], visited)

visited = [-1 for _ in range(n+1)]
for node in circular_nodes:
    visited[node] = 0

for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i, visited)

print(" ".join(map(str, visited[1:])))
