s = input()
b = input()
lb = len(b)
ls = len(s)

stack = []
idx = 0

for i, v in enumerate(s):
    if v == b[-1]:
        isbomb = True
        for j in range(lb - 1):
            if len(stack) >= lb - 1 and stack[len(stack) - lb + j + 1] == b[j]:
                continue
            else:
                isbomb = False
                break
        if isbomb:
            for j in range(lb-1):
                if len(stack) > 0:
                    stack.pop()
        else:
            stack.append(v)
    else:
        stack.append(v)
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))