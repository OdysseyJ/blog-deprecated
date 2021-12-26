from itertools import combinations

nums = [int(input()) for _ in range(9)]

combinate = combinations(nums, 7)
for c in combinate:
    if sum(c) == 100:
        for i in sorted(c):
            print(i)
        break
