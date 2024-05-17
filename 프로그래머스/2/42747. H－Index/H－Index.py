def solution(citations):
    c = sorted(citations, reverse = True)
    for i, v in enumerate(c):
        if i >= v:
            return i
    return len(citations)