h, w = map(int, input().split())
wall = list(map(int, input().split()))

world = [[1] * i + [0] * (h - i) for i in wall]
for i in range(h):
    first = -1
    last = -1
    for j in range(w):
        if world[j][i] == 1:
            first = j
            break
    for j in range(w):
        if world[w - 1 - j][i] == 1:
            last = w - j
            break
    if first == last:
        continue
    for j in range(first, last):
        if world[j][i] == 0:
            world[j][i] = -1

cnt = 0
for i in range(h):
    for j in range(w):
        if world[j][i] == -1:
            cnt += 1
print(cnt)
        