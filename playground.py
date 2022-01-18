import sys

n = int(sys.stdin.readline().strip())
nums = [int(num) for num in input().split(" ")]

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if nums[j] > nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
