n, k = map(int, input().split(" "))

# dp[n][k] = n을 k개의 양의 정수를 가지고 표현하는 경우의 수.
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
DIV = 1000000000

for i in range(1, k+1):
    dp[1][i] = i

for i in range(1, n+1):
    dp[i][1] = 1

for i in range(2, n+1):
    for j in range(2, k+1):
        # i를 j개의 양의 정수를 가지고 표현하려면
        # j개의 양의정수를 가지고 i-1의 수를 표현하는 경우에 전부 1씩을 더하는 케이스
        # j-1개의 양의정수를 가지고 i의 수를 표현하는 경우에 전부 0을 더해주는 케이스
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%DIV

print(dp[n][k]%DIV)
