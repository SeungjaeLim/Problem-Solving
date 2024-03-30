def diff(N, A, B):
    cnt = 0
    for i in range(N):
        for j in range(i+1):
            if A[i][j] != B[i][j]:
                cnt += 1
    return cnt

def poss(A):
    posA = []
    posA.append(A)
    posA.append(flip(A))
    posA.append(rot(A))
    posA.append(flip(rot(A)))
    posA.append(rot(rot(A)))
    posA.append(flip(rot(rot(A))))
    return posA

def rot(A):
    A1 = []
    for i in range(len(A)):
        A1.append([])
    for i in range(len(A)):
        for j in range(i+1):
            A1[N - 1 - j].append(A[i][j])
    return A1

def flip(A):
    A1 = []
    for i in range(len(A)):
        A1.append(A[i][::-1])
    return A1

N = int(input())
A = []
B = []
for i in range(N) :
    A.append(list(map(int,input().split())))
for i in range(N) :
    B.append(list(map(int,input().split())))

posA = poss(A)
posB = poss(B)

score = N * N
for a in posA:
    for b in posB:
        tmp = diff(N,a,b)
        if tmp < score:
            score = tmp
print(score)