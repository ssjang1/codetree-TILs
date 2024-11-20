n,m = map(int,input().strip().split(' '))
A = list(map(int,input().strip().split(' ')))

def answer(A,m):
    value = A[m-1]
    while m != 1:
        if m%2==1:
            m-=1
            m = int(m)
        else:
            m/=2
            m = int(m)
        value += A[m-1]
    return value

print(answer(A,m))