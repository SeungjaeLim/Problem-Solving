def solution(n, times):
    l = 1
    r = max(times) * n
    answer = 0
    while l <= r:
        
        mid = (l + r) // 2
        print(l, r, mid)
        tot = 0
        for i in times:
            tot += mid // i
            
        if tot < n:
            l = mid + 1
        else:
            answer = mid
            r = mid - 1
    
    return answer