n = int(input())
nums = [int(num) for num in input().split(" ")]

dp = [[0 for _ in range(2)] for _ in range(100001)]
dp[0][0] = nums[0]
dp[0][1] = nums[0]

result = max(dp[0])
for i in range(1, n):
    dp[i][0] = max(0, dp[i-1][0]) + nums[i]
    dp[i][1] = max(dp[i-1][1] + nums[i], dp[i-1][0])
    result = max(dp[i][0], dp[i][1], result)

print(result)
