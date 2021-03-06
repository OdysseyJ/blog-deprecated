import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

k = int(input().strip())
lines = [input() for _ in range(k)]
video = [[i for i in line] for line in lines]


def solve(n, x, y):
    if n == 1:
        return video[y][x]
    h = int(n/2)
    a = solve(h, x, y)
    b = solve(h, x+h, y)
    c = solve(h, x, y+h)
    d = solve(h, x+h, y+h)
    if all(map(lambda r: r == "1", [a, b, c, d])):
        return "1"
    if all(map(lambda r: r == "0", [a, b, c, d])):
        return "0"
    return f"({a}{b}{c}{d})"


print(solve(k, 0, 0))
