n = int(input())

mod = 1000000000

# dp[n][i] = n자리 숫자를 가지는 녀석들 중 마지막 수가 i로 끝나는 계단수의 개수
dp = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, 101):
    dp[i][0] = dp[i-1][1] % mod
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
    dp[i][9] = dp[i-1][8] % mod

print(sum(dp[n])%mod)
