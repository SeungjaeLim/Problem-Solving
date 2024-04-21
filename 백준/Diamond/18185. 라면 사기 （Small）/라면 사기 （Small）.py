def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    v = [0] * (n + 3) 
    for i in range(1, n+1):
        v[i] = int(data[i])
    
    ans = 0
    
    for i in range(1, n+1):
        if v[i+1] > v[i+2]:
            a = min(v[i], v[i+1] - v[i+2])
            ans += 5 * a
            v[i] -= a
            v[i+1] -= a
            
            b = min(v[i], min(v[i+1], v[i+2]))
            ans += 7 * b
            v[i] -= b
            v[i+1] -= b
            v[i+2] -= b
        else:
            b = min(v[i], min(v[i+1], v[i+2]))
            ans += 7 * b
            v[i] -= b
            v[i+1] -= b
            v[i+2] -= b
            
            a = min(v[i], v[i+1])
            ans += 5 * a
            v[i] -= a
            v[i+1] -= a
            
        ans += 3 * v[i]
    
    print(ans)

if __name__ == "__main__":
    main()
