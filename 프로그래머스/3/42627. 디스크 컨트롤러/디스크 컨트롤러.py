import heapq

def solution(jobs):
    t = 0
    cur_job = 0
    start_job = 0
    have_job = False
    ans = []
    h = []
    len_jobs = len(jobs)
    
    while(len(ans) < len_jobs):
        exclude = []
        for i, v in enumerate(jobs):
            if v[0] <= t:
                heapq.heappush(h, (v[1], v[0]))
                exclude.append(i)
        tmp_jobs = []
        for i, v in enumerate(jobs):
            if i in exclude:
                continue
            else:
                tmp_jobs.append(v)
        jobs = tmp_jobs
        
                
        if not have_job:
            if h:
                
                cur_job, start_job = heapq.heappop(h)
                #print("get job", [start_job, cur_job])
                have_job = True
        else:    
            if cur_job <= 0:
                ans.append(t - start_job)
                if h:
                    cur_job, start_job = heapq.heappop(h)
                    #print("get job", [start_job, cur_job])
                else:
                    have_job = False
                
        t += 1
        cur_job -= 1
    
    tot = 0
    for i in ans:
        tot += i
    tot //= len(ans)
    return tot