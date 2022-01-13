n = int(input())

# dp[n][i] = i으로 끝나는 n자리 2친수
dp = [[0 for _ in range(3)] for _ in range(91)]

dp[1][0] = dp[2][1] = 0
dp[1][1] = dp[2][0] = 1

for i in range(3, 91):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[n]))
