n = int(input())

def is_vps(string):
    stack = []
    for s in string:
        if s=="(":
            stack.append(s)
        if s==")":
            if not stack:
                return "NO"
            else:
                stack.pop()
    return "YES" if len(stack) == 0 else "NO"

for _ in range(n):
    string = input()
    print(is_vps(string))
