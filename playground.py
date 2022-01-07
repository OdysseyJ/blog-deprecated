import collections
import sys
print("Hello"
      "world")

deque = collections.deque()
n = int(sys.stdin.readline().strip())

for i in range(n):
    line = sys.stdin.readline().strip()

    if line == "pop_front":
        if deque:
            print(deque.popleft())
        else:
            print(-1)
        continue
    if line == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)
        continue
    if line == "size":
        print(len(deque))
        continue
    if line == "empty":
        print(0 if deque else 1)
        continue
    if line == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
        continue
    if line == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)
        continue
    command, num = line.split(" ")
    if command == "push_front":
        deque.appendleft(num)
        continue
    if command == "push_back":
        deque.append(num)
        continue
