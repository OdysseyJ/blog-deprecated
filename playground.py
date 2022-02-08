from collections import deque

n = int(input())

queue = deque([(1, 0)])
time = [[-1 for _ in range(n+1)] for _ in range(n+1)]
time[1][0] = 0

while queue:
    s, c = queue.popleft()

    # 이모티콘 붙여넣기
    if s+c <= n and time[s+c][c] == -1:
        queue.append((s+c, c))
        time[s+c][c] = time[s][c] + 1

    # 이모티콘 하나 삭제
    if s-1>=0 and time[s-1][c] == -1:
        queue.append((s-1, c))
        time[s-1][c] = time[s][c] + 1

    # 클립보드 저장
    if time[s][s] == -1:
        time[s][s] = time[s][c] + 1
        queue.append((s, s))

print(min(list(filter(lambda x:x!=-1, time[n]))))
