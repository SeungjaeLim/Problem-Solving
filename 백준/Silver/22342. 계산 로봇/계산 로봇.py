M, N = map(int, input().split())
inp = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(1, M + 1):
    row = input().strip()
    for j in range(1, N + 1):
        inp[i][j] = int(row[j - 1])

ret = 0
store = [[0] * (N + 1) for _ in range(M + 1)]
print_arr = [[0] * (N + 1) for _ in range(M + 1)]

for j in range(1, N + 1):
    for i in range(1, M + 1):
        for k in range(-1, 2):
            if 1 <= i + k <= M:
                store[i][j] = max(store[i][j], print_arr[i + k][j - 1])
        print_arr[i][j] = store[i][j] + inp[i][j]
        ret = max(ret, store[i][j])

print(ret)