n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(len(arr)):
    if i%2==0:
        print(arr[i//2], end=' ')