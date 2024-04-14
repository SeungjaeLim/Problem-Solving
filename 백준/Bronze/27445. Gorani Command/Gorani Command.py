N, M = map(int, input().split())
x_lst = []
for i in range(N - 1):
    x_lst.append(int(input()))
y_lst = list(map(int, input().split()))
x_lst.append(y_lst[0])
print(x_lst.index(min(x_lst)) + 1, y_lst.index(min(y_lst)) + 1)