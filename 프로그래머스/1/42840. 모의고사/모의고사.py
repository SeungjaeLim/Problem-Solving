def solution(answers):
    answer = []
    m = -1
    cnt = [0,0,0]
    ans = []
    ans.append([1, 2, 3, 4, 5] * 2000)
    ans.append([2, 1, 2, 3, 2, 4, 2, 5] * 1250)
    ans.append([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000)
    for i, v in enumerate(answers):
        for j, k in enumerate(ans):
            if v == k[i]:
                cnt[j] += 1
    for i, v in enumerate(cnt):
        if v > m:
            m = v
            answer = [i+1]
        elif v == m:
            answer.append(i+1)
    return answer