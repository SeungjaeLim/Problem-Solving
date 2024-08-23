dp = [0] * 10001

n, k = map(int, input().split())

v = [0] * (n + 1)
for i in range(1, n + 1):
    v[i] = int(input())

dp[0] = 1

for i in range(1, n + 1):
    for j in range(v[i], k + 1):
        dp[j] += dp[j - v[i]]

print(dp[k])