n = int(input())
expression = input()
values = [int(input()) for _ in range(n)]
d = {}

for idx, value in enumerate(values):
    d[chr(ord("A")+idx)] = value

stack = []

operations = {
    "+": "+",
    "-": "-",
    "*": "*",
    "/": "/",
}

for c in expression:
    if (op := operations.get(c)) is not None:
        after = stack.pop()
        before = stack.pop()
        if op == "+":
            stack.append(before+after)
        elif op == "-":
            stack.append(before-after)
        elif op == "*":
            stack.append(before*after)
        elif op == "/":
            stack.append(before/after)
    else:
        stack.append(d[c])

print(f'{stack[0]:.2f}')
