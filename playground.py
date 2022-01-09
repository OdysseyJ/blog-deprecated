import collections

n, k = map(int, input().split(" "))

queue = collections.deque([(n, int(0))])
visited = [False] * 100001

while queue:
    pos, step = queue.popleft()
    if pos == k:
        print(step)
        break

    for pos in (pos+1, pos-1, pos*2):
        if 0 <= pos and pos <= 100000 and not visited[pos]:
            visited[pos] = True
            queue.append((pos, step+1))
