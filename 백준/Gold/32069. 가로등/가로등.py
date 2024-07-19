def solve(L, N, K, lamps):
    darkness_levels = []
    
    for i in range(N):
        darkness_levels.append(0)
        
    for i in range(1, N):
        mid = (lamps[i-1] + lamps[i]) // 2
        for j in range(lamps[i-1] + 1, mid + 1):
            darkness_levels.append(j - lamps[i-1])
        for j in range(mid + 1, lamps[i]):
            darkness_levels.append(lamps[i] - j)
    
    if lamps[0] > 0:
        for j in range(lamps[0]):
            darkness_levels.append(lamps[0] - j)
    
    if lamps[-1] < L:
        for j in range(lamps[-1] + 1, L + 1):
            darkness_levels.append(j - lamps[-1])
    
    darkness_levels.sort()
    
    for i in range(K):
        print(darkness_levels[i])

L, N, K = map(int, input().split())
lamps = list(map(int, input().split()))
solve(L, N, K, lamps)
