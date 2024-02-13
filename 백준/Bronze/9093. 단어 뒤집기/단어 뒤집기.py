n = int(input())
for i in range(n):
    s = []
    l = input()
    for k in l:
        if k == ' ':
            while len(s) > 0:
                print(s.pop(), end='')
            print(' ', end = '')
        else:
            s.append(k)
    while len(s) > 0:
        print(s.pop(), end='') 
    print("")