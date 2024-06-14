import heapq

def solution(operations):
    mah = []
    mih = []
    l = 0
    for i, v in enumerate(operations):
        cmd, v = v.split()
        if cmd == "I":
            heapq.heappush(mih, int(v))
            heapq.heappush(mah, (-int(v),int(v)))
            l += 1
        elif cmd == "D":
            if v == "-1":
                if l > 0:
                    l -= 1
                    tmp = heapq.heappop(mih)
                    mah.remove((-tmp, tmp))
            elif v == "1":
                if l > 0:
                    l -= 1
                    tmp = heapq.heappop(mah)
                    mih.remove(tmp[1])
    if l == 0:
        return [0,0]
    return [heapq.heappop(mah)[1], heapq.heappop(mih)]
