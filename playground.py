import sys

input = sys.stdin.readline

n = int(input().strip())
nodes = [[] for _ in range(n+1)]
nodes[0].append(1)

for _ in range(n-1):
    n1, n2 = map(int, input().strip().split(" "))
    nodes[n1].append(n2)
    nodes[n2].append(n1)

answer = list(map(int, input().strip().split(" ")))


def find():
    before = [0]
    idx = 0
    for a in answer:
        while a not in nodes[before[idx]]:
            idx += 1
            if idx == len(before):
                return 0
        before.append(a)
    return 1


print(find())
