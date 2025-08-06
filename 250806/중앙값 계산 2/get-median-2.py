n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

# for i in range(len(arr)):
#     if i%2==0:
#         if i!=n-1 or i !=n-2:
#             print(arr[i//2], end=' ')
#         else:
#             print(arr[i//2])  중앙값이 값의 크기의 중앙값이었음

for i in range(len(arr)):
    if i%2==0:
        check = arr[:i+1]
        check.sort()
        print(check[i//2],end=' ')