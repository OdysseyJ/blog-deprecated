import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

n, m = map(int, input().strip().split(" "))
boards = [[i for i in input().strip()] for _ in range(n)]

def is_valid(x, y):
    if 0 <= x < m and 0 <= y < n:
        return True
    return False


def dfs(x, y, b_x, b_y, visited, cnt):
    global result

    if visited[y][x] != '0':
        return
    visited[y][x] = boards[y][x]

    for x_add, y_add in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x = x+x_add
        new_y = y+y_add
        if is_valid(new_x, new_y):
            if cnt >= 4 and visited[new_y][new_x] == boards[y][x] and (new_y != b_y or new_x != b_x):
                result = 1
            if boards[new_y][new_x] == boards[y][x] and visited[new_y][new_x] == '0' and (new_y != b_y or new_x != b_x):
                dfs(new_x, new_y, x, y, visited, cnt + 1)

result = 0
visited = [['0' for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        dfs(j, i, 0, 0, visited, 1)
        if result:
            print("Yes")
            break
    if result:
        break
if not result:
    print("No")
