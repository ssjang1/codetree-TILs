arr2d = [[1 for i in range(5)]for i in range(5)]

for i in range(1,5):
    for j in range(1,5):
        arr2d[i][j] = arr2d[i-1][j] + arr2d[i][j-1]

for i in range(5):
    for j in range(5):
        print(arr2d[i][j],end=' ')
    print()