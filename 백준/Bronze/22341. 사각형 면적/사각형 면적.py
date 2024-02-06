n, c = map(int, input().split())
h, w = n, n
for i in range(c):
    a, b = map(int, input().split())
    if a < h and b < w:
        if a * w >= b * h:
            h = a
        else:
            w = b
print(w*h)
            