t = int(input())
coin = [25, 10, 5, 1]

for i in range(t):
    cnt = [0, 0, 0, 0]
    c = int(input())
    for j, v in enumerate(coin):
        cnt[j] = c // coin[j]
        c = c % coin[j]
    for k in cnt:
        print(k, end=' ')
    print("")
    
