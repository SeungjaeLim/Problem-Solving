class Conference:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def cmp(conf):
    return (conf.end, conf.start)

def main():
    n = int(input())
    conflist = []
    
    for _ in range(n):
        s, e = map(int, input().split())
        conflist.append(Conference(s, e))
    
    conflist.sort(key=cmp)
    
    cnt = 0
    tmp = 0
    
    for conf in conflist:
        if tmp <= conf.start:
            tmp = conf.end
            cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    main()
