def solution(numbers):
    l = get_possible(numbers)
    answer = 0
    for i in l:
        if (is_prime(i)):
            answer += 1
    return answer

def get_possible(numbers):
    l = []
    for j in range(len(numbers)):
        for k in range(len(numbers)):
            tmp = list(numbers)
            tmp.pop(k)
            l.extend(get_num(numbers[k], tmp, j + 1))
    for i, v in enumerate(l):
        l[i] = int(v)
    l = list(set(l))
    return l

def get_num(cur, pos, n):
    if n == 1:
        return [str(cur)]
    
    if len(cur) == n:
        return [str(cur)]
    l = []
    for i, v in enumerate(pos):
        tmpcur = cur[:]
        tmpcur += str(v)
        tmp = pos[:]
        tmp.pop(i)
        l.extend(get_num(tmpcur, tmp, n))
    return l

def is_prime(n):
    if n == 0 or n == 1:
        return False
    cnt = 2
    while cnt ** 2 <= n:
        if n % cnt == 0:
            return False
        cnt += 1
    return True
        
        