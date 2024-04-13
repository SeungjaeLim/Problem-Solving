def solution(sizes):
    w = 0
    h = 0
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
        if w < i[0]:
            w = i[0]
        if h < i[1]:
            h = i[1]

    return w * h