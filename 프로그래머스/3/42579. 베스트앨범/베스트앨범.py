def solution(genres, plays):
    totplay = {}
    for i in range(len(genres)):
        if genres[i] in totplay:
            totplay[genres[i]] += plays[i]
        else:
            totplay[genres[i]] = plays[i]
    unique_genres = sorted(genres, reverse = True, key = lambda x: totplay[x])
    d = {}
    bef_genres = ""
    cnt = 0
    for i in unique_genres:
        if i == bef_genres:
            continue
        else:
            bef_genres = i
            d[i] = cnt
            cnt += 1
    order = []
    for i in range(len(set(genres))):
        order.append([])
    for i in range(len(genres)):
        order[d[genres[i]]].append([i, plays[i]])
    for i in range(len(order)):
        order[i].sort(reverse = True, key = lambda x: (x[1], -x[0]))
    ans = []
    for o in order:
        for j in range(2):
            if len(o) <= j:
                break
            ans.append(o[j][0])
    return ans
        
    
        