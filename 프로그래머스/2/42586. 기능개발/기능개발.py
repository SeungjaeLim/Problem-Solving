
def solution(progresses, speeds):
    
    answer = []
    wq = []
    for i in range(len(progresses)):
        wq.append([progresses[i], speeds[i]])
    
    cnt = 0
    prev = True
    while len(wq) > 0:
        for i in range(len(wq)):
            w = wq[0]
            wq.pop(0)
            w[0] += w[1]
            if w[0] >= 100 and prev:
                cnt += 1
            else:
                prev = False
                wq.append(w)
        if cnt != 0:
            answer.append(cnt)
        cnt = 0
        prev = True
        
    return answer