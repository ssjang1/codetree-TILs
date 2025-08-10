N = int(input())

# arr = [[i for i in range(1,1+N)] for j in range(N)]
arr = [i for i in range(1,1+N)]

for i in range(N):
    for j in range(N):
        if i%2==0:
            print(arr[j],end='')
        else:
            print(arr[::-1][j],end='')
    print()
        
        