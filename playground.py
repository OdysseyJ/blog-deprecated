import sys

string = sys.stdin.readline().strip()
count = int(sys.stdin.readline().strip())

left = [c for c in string]
right = []

for _ in range(count):
    command = sys.stdin.readline().strip()
    if command == "L":
        if left:
            right.append(left.pop())
        continue
    if command == "D":
        if right:
            left.append(right.pop())
        continue
    if command == "B":
        if left:
            left.pop()
        continue
    added = command.split(" ")[1]
    left.append(added)

print("".join(left+list(reversed(right))))
