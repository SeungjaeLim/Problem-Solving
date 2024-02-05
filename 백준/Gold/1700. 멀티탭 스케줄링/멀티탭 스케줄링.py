n, k = map(int, input().split())
l = list(map(int, input().split()))

cur = []
tot = 0

for i, p in enumerate(l):
    if p in cur:
        continue
    elif len(cur) < n:
        cur.append(p)
    else:
        cnt = [101] * n
        for idx, job in enumerate(cur):
            for j in range(i+1, k):
                if l[j] == job:
                    cnt[idx] = j
                    break
        maxcnt = max(cnt)
        for ic, c in enumerate(cnt):
            if maxcnt == c:
                cur[ic] = p
                tot += 1
                break
print(tot)
            