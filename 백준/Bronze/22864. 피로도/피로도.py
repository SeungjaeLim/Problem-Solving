a, b, c, m = map(int, input().split())
tot = 0
fat = 0
for i in range(24):
    if fat + a > m:
        fat -= c
        if fat < 0:
            fat = 0
    else:
        tot += b
        fat += a
print(tot)
            