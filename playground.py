n = int(input())
nums = [int(i) for i in input().split(" ")]

dp = [1 for _ in range(n)]
dp_r = [1 for _ in range(n)]

def lis(n, nums, dp):
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp

dp = lis(n, nums, dp)
dp_r = lis(n, list(reversed(nums)), dp_r)

result = max([a+b for a, b in zip(dp, list(reversed(dp_r)))])-1
print(result)
