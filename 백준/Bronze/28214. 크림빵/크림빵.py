n, k, p = map(int, input().split())
b = list(map(int,input().split()))

tot = 0

for i in range(n):
    cnt = 0
    for j in range(k):
        if b[k*i + j] == 0:
            cnt += 1
    if cnt < p:
        tot += 1
        
print(tot)