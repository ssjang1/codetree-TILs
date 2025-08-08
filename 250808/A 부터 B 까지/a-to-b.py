A, B = map(int, input().split(' '))

n = A

while n <= B:
    print(n, end=' ')
    if n % 2 == 1:
        n *= 2
    else:
        n +=3 