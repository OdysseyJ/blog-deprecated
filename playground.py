n, k = map(int, input().split(" "))

queue = [str(i) for i in range(1, n+1)]
result = []

while queue:
    for i in range(k-1):
        queue.append(queue.pop(0))
    result.append(queue.pop(0))

answer = ", ".join(result)
print('<{}>'.format(answer))
