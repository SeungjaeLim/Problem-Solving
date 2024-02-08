n = int(input())
l = list(map(int, input().split()))

h = -1
mcnt = 0
cnt = 0

for i, v in enumerate(l):
    if v >= h:
        h = v
        cnt = 0
    else:
        cnt += 1
        if cnt >= mcnt:
            mcnt = cnt

print(mcnt)
