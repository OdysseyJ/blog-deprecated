from collections import deque
check = [False] * 100001
dist = [-1] * 100001

n, k = map(int, input().split())
queue = deque([n])
check[n] = True
dist[n] = 0

while queue:
    now = queue.popleft()
    if now*2 < 100001 and not check[now*2]:
        queue.appendleft(now*2)
        check[now*2] = True
        dist[now*2] = dist[now]
    if now + 1 < 100001 and not check[now+1]:
        queue.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now] + 1
    if now - 1 >= 0 and not check[now-1]:
        queue.append(now-1)
        check[now-1] = True
        dist[now-1] = dist[now] + 1

print(dist[k])
