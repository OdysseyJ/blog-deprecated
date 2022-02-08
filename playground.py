from collections import deque

MAX = 100001
n, k = map(int, input().split(" "))
step = [0 for _ in range(MAX)]
moved = [0 for _ in range(MAX)]

def bfs(start):
    queue = deque([start])
    while queue:
        top = queue.popleft()

        if top == k:
            time = step[top]
            result = []
            for _ in range(time+1):
                result.append(top)
                top = moved[top]
            print(time)
            print(" ".join(map(str, result[::-1])))
            break

        for i in [top+1, top-1, top*2]:
            if 0 <= i < MAX and step[i] == 0:
                queue.append(i)
                step[i] = step[top] + 1
                moved[i] = top

bfs(n)
