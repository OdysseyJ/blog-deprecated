n = int(input())
nums = [int(input()) for _ in range(n)]
stack = []
result = []
history = []
visited = [False]*(n+1)

before = 1
for num in nums:
    if num >= before:
        while num != before:
            if not visited[before]:
                history.append("+")
                stack.append(before)
                visited[before] = True
            before += 1
        result.append(num)
        history.append("+")
        history.append("-")
        visited[num] = True
    elif num < before:
        if stack and stack[-1] == num:
            result.append(stack.pop())
            history.append("-")
        else:
            break

    if num == n:
        while stack:
            result.append(stack.pop())
            history.append("-")
        break
    before = num

if nums == result:
    for h in history:
        print(h)
else:
    print("NO")
