def solve(a, b, c):
    if b == 1:
        return a
    half = solve(a, int(b/2), c)
    result = half * half % c
    if b % 2 != 0:
        result = result * a % c
    return result


a, b, c = map(int, input().split(" "))

print(solve(a, b, c))