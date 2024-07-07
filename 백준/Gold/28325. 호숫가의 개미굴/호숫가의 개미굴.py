n = int(input())
c = list(map(int, input().split()))

tot = sum(c)
if tot == 0:
    print(n // 2)
else:
    start = 0
    for i, v in enumerate(c):
        if v != 0:
            start = i
            break
    c = c[start + 1:] + c[:start + 1]
    visit = [False] * n
    for i in range(n):
        if visit[i] or c[i] != 0:
            continue
        for j in range(i, n):
            if c[j]:
                break
            visit[j] = True
        tot += (j - i + 1) // 2
    print(tot)
        