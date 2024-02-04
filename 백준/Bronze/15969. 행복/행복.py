n = int(input())
maxh = -1
minh = 1001
l = list(map(int, input().split()))
for i in l:
    if maxh < i:
        maxh = i
    if minh > i:
        minh = i
print(maxh - minh)