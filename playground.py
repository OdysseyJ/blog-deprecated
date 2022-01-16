n = int(input())
nums = [int(num) for num in input().split(" ")]
dp = [0 for _ in range(n)]
history = [i for i in range(n)]

idx = 0
max_ = 0
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and dp[j] > dp[i]:
            dp[i] = dp[j]
            history[i] = j
    dp[i] += 1

    if max_ < dp[i]:
        max_ = dp[i]
        idx = i

path = []
while idx != history[idx]:
    path.append(str(nums[idx]))
    idx = history[idx]
path.append(str(nums[idx]))

print(max_)
print(" ".join(path[::-1]))
