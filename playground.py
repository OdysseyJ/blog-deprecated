n = int(input())
queue = []

for i in range(n):
    command = input()
    if command == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    if command == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    if command == "size":
        print(len(queue))
    if command == "empty":
        print(1 if queue else 0)
        continue
    if command == "pop":
        if queue:
            print(queue.remove(0))
        continue
    num = command.split(" ")[1]
    print(num)
    queue.append(num)
