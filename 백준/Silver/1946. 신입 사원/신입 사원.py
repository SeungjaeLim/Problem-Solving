import sys
input = sys.stdin.readline

n = int(input().rstrip())
for i in range(n):
    k =  int(input().rstrip())
    app = []
    hire = 0
    for j in range(k):
        app.append(list(map(int, input().rstrip().split())))
    app = sorted(app, key=lambda x:x[0])
    maxsc = app[0][1]
    for ap in app:
        if ap[1] <= maxsc:
            maxsc = ap[1]
            hire += 1
    print(hire)