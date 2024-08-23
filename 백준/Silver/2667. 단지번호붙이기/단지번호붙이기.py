dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
a = [list(map(int, input().strip())) for _ in range(n)]

def bfs(x, y, cnt):
    if a[x][y] == 2:
        return cnt
    a[x][y] = 2
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == 1:
                cnt = bfs(nx, ny, cnt + 1)
    return cnt

cnt = 1
ans = []

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            cnt = bfs(i, j, cnt)
            ans.append(cnt)
            cnt = 1

ans.sort()
print(len(ans))
for x in ans:
    print(x)
