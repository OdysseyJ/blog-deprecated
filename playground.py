import sys

n = int(input())
queue = []

for i in range(n):
    command = sys.stdin.readline().strip()
    if command == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
        continue
    if command == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
        continue
    if command == "size":
        print(len(queue))
        continue
    if command == "empty":
        print(0 if queue else 1)
        continue
    if command == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
        continue
    num = command.split(" ")[1]
    queue.append(num)
