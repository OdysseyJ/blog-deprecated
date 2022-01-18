import math

n = int(input())

def factorization(n):
    result, temp, i = [], n, 2
    while temp != 1:
        if (temp % i == 0):
            temp /= i
            result.append(i)
        else:
            i += 1
    return result

# 에라토스테네스의 체
MAX = 1000001 # sqrt(1조)+1
PRIME = True
NON_PRIME = False
p = [PRIME] * MAX
p[0] = NON_PRIME
p[1] = NON_PRIME

for i in range(2, MAX):
    if p[i] == PRIME:
        for j in range(2*i, MAX, i):
            p[j] = NON_PRIME

if p[n] == PRIME:
    print(-1)
else:
    i = 2
    result = []
    num = n
    while num != 0 and i < MAX and i <= n:
        if (num % i) == 0:
            result.append(i)
            num = num / i
            i = 2
        else:
            i += 1

    printer = []
    for a, b in zip(result[::2], result[1::2]):
        printer.append(a*b)

    if len(result) % 2 != 0:
        if printer:
            printer[-1] *= result[-1]
        else:
            printer.append(result[-1])

    print(" ".join(map(str, printer)))
