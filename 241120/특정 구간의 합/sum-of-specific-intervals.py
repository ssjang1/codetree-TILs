n,m = map(int,input().strip().split(' '))

A = list(map(int,input().strip().split(' ')))

def answer(m):
    for i in range(m):
        a,b = map(int,input().strip().split(' '))
        value = 0
        for j in range(a,b+1):
            value += A[j-1]
        print(value)

answer(m)
