l = list(input())
n = int(input())
s = []
for i in range(n):
    k = input()
    if k == "L":
        if len(l)>0:
            s.append(l.pop())
    elif k == "D":
        if len(s) > 0:
            l.append(s.pop())
    elif k == "B":
        if len(l)>0:
            l.pop()
    else:
        l.append(k[2])
s.reverse()
print("".join(l+s))