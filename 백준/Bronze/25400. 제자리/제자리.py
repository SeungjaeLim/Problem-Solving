n = int(input())
l = list(map(int, input().split()))

idx = 1
cnt = 0

for i in l:
    if i == idx:
        idx += 1
    else:
        cnt += 1

print(cnt)
    
        