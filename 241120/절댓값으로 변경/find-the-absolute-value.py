n = int(input())
arr = list(map(int,input().strip().split(' ')))
def ab(arr):
    for i in arr:
        if i>=0:
            print(i,end=' ')
        else:
            print(-i,end=' ')

ab(arr)