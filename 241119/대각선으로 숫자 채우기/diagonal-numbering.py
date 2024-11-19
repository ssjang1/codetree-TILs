n, m = map(int,input().strip().split(' '))

line_cnt = n+m-1

arr2d = [[0 for _ in range(m)] for _ in range(n)]

num = 1

for l in range(line_cnt):
    for i in range(0, l + 1):  
        j = l - i  
        if i < n and j < m:  
            arr2d[i][j] = num
            num += 1


# for l in range(line_cnt):
#     for i in range(0,l):
#         for j in range(0,l):
#             if i+j ==l and i<n and j<m:
#                 arr2d[i][j] = num
#                 num +=1
                
for row in arr2d:
    for elem in row:
        print(elem, end=' ')
    print()
