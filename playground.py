n = int(input())
nums = [int(input()) for _ in range(n)]

for num in nums:
    stack = [1, 2, 3]
    count = 0
    while stack:
        top = stack.pop()
        if top == num:
            count += 1
        elif top < num:
            stack.append(top+1)
            stack.append(top+2)
            stack.append(top+3)
    print(count)
