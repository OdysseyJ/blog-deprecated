m, n = map(int, input().split(" "))

DECIMAL = 1
NON_DECIMAL = 0
dp = [DECIMAL] * (n+1)
dp[1] = NON_DECIMAL
for i in range(2, n+1):
    if dp[i] == DECIMAL:
        for j in range(i*i, n+1, i):
            dp[j] = NON_DECIMAL

count = 0
for num in range(m, n+1):
    if dp[num] == DECIMAL:
        print(num)
