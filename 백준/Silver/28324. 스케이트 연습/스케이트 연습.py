n = int(input())
v = list(map(int, input().split()))

s, t = 0, 0
v = v[::-1]
for i in v:
    if s < i:
        s += 1
    else:
        s = i
    t += s
print(t)