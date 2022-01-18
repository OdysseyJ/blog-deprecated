import math

def is_prime(n):
    if n == 1:
        return False
    MAX = int(math.sqrt(n))+1
    for i in range(2, MAX):
        if (n % i) == 0:
            return False
    return True


def factorization_before(n):
    result = []
    temp, i = n, 2
    while temp != 1:
        if temp % i == 0:
            result.append(i)
            temp = int(temp/i)
        else:
            i += 1
    return result

def factorization(n):
    result = []
    temp, i = n, 2
    while temp != 1 and i < math.sqrt(n)+1:
        if temp % i == 0:
            result.append(i)
            temp = int(temp/i)
        elif i == 2:
            i += 1
        else:
            i += 2

    # 소인수가 너무 커서 sqrt(n)에 들어가지 못하는 경우... 망할녀석
    if temp != 1 and is_prime(temp):
        result.append(temp)
    return result

n = int(input())

if is_prime(n):
    print(-1)
else:
    result = factorization(n)
    printer = []
    for even, odd in zip(result[::2], result[1::2]):
        printer.append(even*odd)

    if len(result) % 2 != 0:
        if printer:
            printer[-1] *= result[-1]
        else:
            printer.append(result[-1])

    print(" ".join(map(str, printer)))
