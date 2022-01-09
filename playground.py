sentence = input()

stack = []
operators = {
    "+": 1,
    "-": 1,
    "(": 0,
    ")": 0,
    "*": 2,
    "/": 2
}
result = ""

for c in sentence:
    if (priority := operators.get(c)) is not None:
        if c == "(":
            pass
        elif c == ")":
            while (top := stack.pop()) != "(":
                result += top
            continue
        else:
            while stack and operators[stack[-1]] >= priority:
                result += stack.pop()
        stack.append(c)
    else:
        result += c

while stack:
    result += stack.pop()

print(result)
