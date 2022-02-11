import sys
sys.setrecursionlimit(100000)

k = int(input())
stars = [[" " for _ in range(k)] for _ in range(k)]


def solve(x, y, n):
    if n == 1:
        stars[y][x] = "*"
        return

    d = int(n/3)
    solve(x, y, d)
    solve(x, y+d, d)
    solve(x, y+d+d, d)
    solve(x+d, y, d)
    # 가운데 생략
    solve(x+d, y+d+d, d)
    solve(x+d+d, y, d)
    solve(x+d+d, y+d, d)
    solve(x+d+d, y+d+d, d)


solve(0, 0, k)
for i in range(k):
    print("".join(stars[i]))
