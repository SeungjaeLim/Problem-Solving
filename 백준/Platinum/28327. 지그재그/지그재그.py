def main():
    import sys
    input = sys.stdin.read
    from bisect import insort, bisect_left
    from itertools import islice

    data = input().split()
    
    N = int(data[0])
    a = [0] * (N + 1)
    pos = [0] * (N + 1)
    
    for i in range(1, N + 1):
        a[i] = int(data[i])
    for i in range(1, N + 1):
        pos[a[i]] = i
    
    s = []
    ans = 0

    def update(p_index):
        if p_index >= len(s) - 2:
            return 0
        if (s[p_index][1] < s[p_index + 1][1]) != (s[p_index + 1][1] < s[p_index + 2][1]):
            return 0
        return s[p_index][0] * (N - s[p_index + 2][0] + 1)
    
    for i in range(1, N + 1):
        p = bisect_left(s, (pos[i], 0))

        if p > 0:
            ans += update(p - 1)
            if p > 1:
                ans += update(p - 2)

        insort(s, (pos[i], i))
        ans += pos[i] * (N - pos[i] + 1)

        p = bisect_left(s, (pos[i], 0))

        ans -= update(p)
        if p > 0:
            ans -= update(p - 1)
            if p > 1:
                ans -= update(p - 2)

        print(ans)

if __name__ == "__main__":
    main()
