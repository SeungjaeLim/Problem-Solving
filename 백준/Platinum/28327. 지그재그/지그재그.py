import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
arr = [0] * (n + 1)
g = [0] * (n + 1)

for i in range(1, n + 1):
    arr[i] = int(data[i])

for x in range(1, n + 1):
    for y in range(1, n + 1):
        v = []
        dir = 0
        
        for z in range(y, n + 1):
            cur = arr[z]
            if cur <= x:
                if len(v) < 2:
                    v.append(cur)
                    if len(v) == 2:
                        dir = 1 if v[0] > v[1] else -1
                else:
                    nxt_dir = 1 if v[-1] > cur else -1
                    if dir != nxt_dir:
                        v.append(cur)
                        dir = nxt_dir
                    else:
                        v[-1] = cur
            
            g[x] += len(v)

for i in range(1, n + 1):
    print(g[i])
