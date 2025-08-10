N = int(input())

arr = [i for i in range(1,1+N)]

for i in range(N):
    for j in range(N):
        if j%2 ==0:
            print(arr[i],end='')
        else:
            print(arr[-1-i],end='')
    print()