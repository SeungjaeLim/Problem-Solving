n, m, k = map(int, input().split())
board = []
dp = [[False for i in range(m)] for j in range(n)]

for i in range(n):
    board.append(list(input().rstrip()))

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if dp[i][j] or board[i][j] == '#':
            continue
        if i > 0:
            dp[i-1][j] = True
        if j > 0:
            dp[i][j-1] = True
        for k in range(1, k+1):
            if i-k >= 0 and j - k >= 0:
                dp[i-k][j-k] = True

ans = []

n_q = int(input())
for i in range(n_q):
    x, y = map(int, input().split())
    if dp[x-1][y-1]:
        print('First')
    else:
        print('Second')
