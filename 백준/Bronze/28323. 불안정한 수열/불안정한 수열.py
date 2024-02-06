n = int(input())
l = list(map(int, input().split()))


olen = 0
elen = 0

odd = False
for i in l:
    if odd and i%2 == 0:
        olen += 1
        odd = False
    elif not odd and i%2 == 1:
        olen += 1
        odd = True

odd = True
for i in l:
    if odd and i%2 == 0:
        elen += 1
        odd = False
    elif not odd and i%2 == 1:
        elen += 1
        odd = True

print(max([olen, elen, 1]))
        