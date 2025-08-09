N, M = map(int,input().split(' '))

arr1 = [list(map(int,input().strip().split(' '))) for _ in range(N)]

arr2 = [list(map(int,input().strip().split(' '))) for _ in range(N)]

result = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr1[i][j] != arr2[i][j]:
            result[i][j] = 1

for row in result:
    for elem in row:
        print(elem, end=' ')
    print()