import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    m1 = scoville[0]
    answer = 0
    while m1 < K and len(scoville) > 1:
        m1 = heapq.heappop(scoville)
        m2 = heapq.heappop(scoville)
        heapq.heappush(scoville, m1 + 2 * m2)
        answer += 1
        m1 = scoville[0]
        if len(scoville) == 1:
            break
    if m1 < K:
        return -1
    else:
        return answer