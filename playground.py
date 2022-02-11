n = int(input())

for i in range(n):
    print("".join(["*" for _ in range(n-i)]))