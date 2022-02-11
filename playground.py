import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(visited[i]+" ", end="")
        print()
        return
    for i in range(start, len(s)):
        visited[depth] = s[i]
        dfs(i+1, depth+1)


while True:
    line = input().strip().split(" ")
    n = int(line[0])
    if n == 0:
        break
    visited = [0 for _ in range(n)]
    s = line[1:]
    dfs(0, 0)
    print()