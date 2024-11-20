N = int(input())

def a1(n):
    if n==0:
        return
    a1(n-1)
    print(n, end=' ')

def a2(n):
    if n==0:
        return
    print(n, end=' ')
    a2(n-1)

a1(N)
print()
a2(N)