import sys
from collections import deque
input = sys.stdin.readline

def bipartite_graph(start_node, visited):
    queue = deque([(start_node, 1)])
    visited[start_node] = 1

    while queue:
        node, flag = queue.popleft()
        for linked_node in nodes[node]:
            if visited[linked_node] == 0:
                queue.append((linked_node, -flag))
                visited[linked_node] = -flag
            elif visited[linked_node] == flag:
                return False
    return True

k = int(input().strip())
for _ in range(k):
    v, e = map(int, input().strip().split(" "))
    nodes = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]

    for i in range(e):
        n1, n2 = map(int, input().strip().split(" "))
        nodes[n1].append(n2)
        nodes[n2].append(n1)

    print("YES" if all(
        [bipartite_graph(i, visited) for i in range(1, v+1) if visited[i] == 0]
    ) else "NO")
