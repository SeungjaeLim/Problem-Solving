import sys
input = sys.stdin.readline

n = input().rstrip()
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

a = sorted(a)
b = sorted(b, reverse = True)
res = sum(a[i] * b[i] for i in range(len(a)))

print(res)