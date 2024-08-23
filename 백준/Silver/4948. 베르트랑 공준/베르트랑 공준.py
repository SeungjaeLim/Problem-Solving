import math

def eratos(is_prime, n):
    for i in range(2, n):
        is_prime[i] = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return is_prime

input_list = []
is_prime = [False] * 246913

while True:
    num = int(input())
    if num == 0:
        break
    input_list.append(num)
    
l = eratos(is_prime, 246913)

for num in input_list:
    cnt = 0
    for k in range(num + 1, 2 * num + 1):
        if l[k]:
            cnt += 1
    print(cnt)
