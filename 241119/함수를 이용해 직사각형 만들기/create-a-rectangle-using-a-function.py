def make_square(n,m):
    for i in range(n):
        for j in range(m):
            print(1,end='')
        print()

n,m = map(int,input().split(' '))
make_square(n,m)