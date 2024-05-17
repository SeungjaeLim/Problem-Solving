def solution(numbers):
    n = sorted(numbers, reverse = True, key = lambda x: (str(x) * 3))
    ans = ""
    for i in n:
        ans += str(i)
    if int(ans) == 0:
        ans = "0"
    return ans

    