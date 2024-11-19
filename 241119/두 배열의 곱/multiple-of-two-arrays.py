line1 = list(map(int,input().strip().split(' ')))
line2 = list(map(int,input().strip().split(' ')))
line3 = list(map(int,input().strip().split(' ')))

_ = input()

line4 = list(map(int,input().strip().split(' ')))
line5 = list(map(int,input().strip().split(' ')))
line6 = list(map(int,input().strip().split(' ')))

arr1 = [line1,line2,line3]
arr2 = [line4,line5,line6]

for i in range(3):
    for j in range(3):
        print(arr1[i][j]*arr2[i][j],end=' ')
    print()