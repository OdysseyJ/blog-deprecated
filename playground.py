n = int(input())
nums = [int(i) for i in input().split(" ")]

d = {}
for num in nums:
    if d.get(num) is None:
        d[num] = 1
    else:
        d[num] += 1

result = [-1] * n
stack = []

for i in range(n):
    while stack and d[nums[stack[-1]]] < d[nums[i]]:
        result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)
