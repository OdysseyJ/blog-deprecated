from itertools import product

n, m = map(int, input().split(" "))

a = []
for _ in range(m):
    a.append([str(i) for i in range(1, n+1)])

product_ = product(*a)

for p in list(product_):
    print(" ".join(p))
