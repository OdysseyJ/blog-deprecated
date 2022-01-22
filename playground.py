from itertools import permutations

n = int(input())
nums = [int(n) for n in input().split(' ')]

perms = permutations(nums, n)

max = 0
for perm in perms:
    diff = 0
    for j in range(len(perm)-1):
        diff += abs(perm[j] - perm[j+1])

    if diff > max:
        max = diff

print(max)
