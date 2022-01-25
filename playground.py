import sys

n = int(sys.stdin.readline().strip())
nums = [[int(n) for n in sys.stdin.readline().strip().split(" ")] for _ in range(n)]

RED = 0
GREEN = 1
BLUE = 2

def rgb_distance(k):
    dp = [[0 for _ in range(3)] for _ in range (n+1)]
    for i in range(3):
        if i == k:
            dp[1][i] = 1001
        else:
            dp[1][i] = nums[0][i]

    for i in range(2, n+1):
        dp[i][RED] = min(dp[i-1][GREEN], dp[i-1][BLUE]) + nums[i-1][0]
        dp[i][GREEN] = min(dp[i-1][RED], dp[i-1][BLUE]) + nums[i-1][1]
        dp[i][BLUE] = min(dp[i-1][RED], dp[i-1][GREEN]) + nums[i-1][2]

    return dp[n][k]

print(min(rgb_distance(0), rgb_distance(1), rgb_distance(2)))
