n = int(input())

idx = 0
i = 666

while True:
    tmp = i
    while tmp >= 666:
        if tmp % 1000 == 666:
            idx += 1
            break
        tmp = tmp // 10
    
    if idx == n:
        break
    
    i += 1

print(i)
