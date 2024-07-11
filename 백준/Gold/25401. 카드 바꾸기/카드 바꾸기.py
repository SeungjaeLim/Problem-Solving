N = int(input())

arr = [0] + list(map(int, input().split()))

ans = 500
for i in range(1, N):
    for j in range(i + 1, N + 1):
        diff = (arr[j] - arr[i]) / (j - i)

        if diff - int(diff) != 0:
            continue
        
        cnt = 0
        s = arr[i] - diff * i
        for k in range(1, N + 1):
            s += diff
            if arr[k] != s:
                cnt += 1

        ans = min(ans, cnt)
print(ans)
