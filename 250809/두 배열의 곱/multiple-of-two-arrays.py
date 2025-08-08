arr1 = [list(map(int,input().split(' '))) for _ in range(3)]

blank = input()

arr2 = [list(map(int,input().split(' '))) for _ in range(3)]

result = [[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        result[i][j] = arr1[i][j] * arr2[i][j]

for row in result:
    for element in row:
        print(element, end=' ')
    print()
