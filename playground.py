n = int(input())

s = 0
for i in range(1, n+1):
    if s+i == n:
        print(i)
        break
    elif s+i > n:
        print(i-1)
        break
    else:
        s += i
