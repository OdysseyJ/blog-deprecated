import sys

count = int(sys.stdin.readline().strip())

stack = []
for i in range(count):
    command = sys.stdin.readline().strip()
    if command == "pop":
        print(stack.pop() if stack else -1)
        continue
    if command == "size":
        print(len(stack))
        continue
    if command == "empty":
        print(1 if not stack else 0)
        continue
    if command == "top":
        print(stack[-1] if stack else -1)
        continue
    num = command.split(" ")[1]
    stack.append(num)
