import sys

mod = 1000000009
t = int(input())

# dp[n][i] = 합의 마지막 수가 i일때, [1,2,3]을 이용해 n을 만드는 방법
dp = [[0 for _ in range(4)] for _ in range(100001)]

dp[1][1] = dp[2][2] = dp[3][1] = dp[3][2] = dp[3][3] = 1

for i in range(4, 100001):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % mod
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % mod
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % mod

for i in range(t):
    n = int(sys.stdin.readline().strip())
    print(sum(dp[n])%mod)
