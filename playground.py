def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

n, s = map(int, input().split(" "))
nums = map(int, input().split(" "))

if n==1:
    print(list(nums)[0]-s)
else:
    diffs = set([abs(num-s) for num in nums])
    d = min(diffs)
    for diff in diffs:
        d = gcd(d, diff)
    print(d)
