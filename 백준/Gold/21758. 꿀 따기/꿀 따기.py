n = int(input())
v = [0] * (n + 1)
sum_ = [0] * (n + 1)
elements = list(map(int, input().split()))

for i in range(1, n + 1):
    v[i] = elements[i - 1]
    sum_[i] = v[i] + sum_[i - 1]

ans = 0

for i in range(2, n):
    ans = max(ans, sum_[n] - v[1] - v[i] + sum_[n] - sum_[i])

for i in range(2, n):
    ans = max(ans, sum_[n] - v[n] - v[i] + sum_[i - 1])

for i in range(2, n):
    ans = max(ans, sum_[i] - v[1] + sum_[n] - sum_[i - 1] - v[n])

print(ans)
