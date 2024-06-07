def change_start_black(x, y, chess_board):
    cnt = 0
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            if (i + j) % 2 == 0:
                if chess_board[i][j] != 'B':
                    cnt += 1
            else:
                if chess_board[i][j] != 'W':
                    cnt += 1
    return cnt

def change_start_white(x, y, chess_board):
    cnt = 0
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            if (i + j) % 2 == 0:
                if chess_board[i][j] != 'W':
                    cnt += 1
            else:
                if chess_board[i][j] != 'B':
                    cnt += 1
    return cnt


n, m = map(int, input().split())
chess_board = [input().strip() for _ in range(n)]
cnt = 100000

for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        tmp = change_start_black(j, i, chess_board)
        if tmp < cnt:
            cnt = tmp
        tmp = change_start_white(j, i, chess_board)
        if tmp < cnt:
            cnt = tmp

print(cnt)
