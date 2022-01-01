from itertools import permutations

n, m = map(int, input().split(" "))

permutation = permutations([str(i) for i in range(1, n+1)], m)

for p in sorted(set(map(lambda x:" ".join(sorted(x)), list(permutation)))):
    print(p)
