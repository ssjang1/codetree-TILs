n,m= map(int,input().strip().split(' '))
arr1=list()
arr2=list()
for _ in range(n):
    line = list(map(int,input().strip().split(' ')))
    arr1.append(line)

for _ in range(n):
    line = list(map(int,input().strip().split(' ')))
    arr2.append(line)

zero_arr = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            zero_arr[i][j] = 0
        else:
            zero_arr[i][j] = 1

for i in range(n):
    for j in range(m):
        print(zero_arr[i][j], end = ' ')
    print()