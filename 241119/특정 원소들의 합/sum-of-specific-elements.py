line1=list(map(int,input().strip().split(' ')))
line2=list(map(int,input().strip().split(' ')))
line3=list(map(int,input().strip().split(' ')))
line4=list(map(int,input().strip().split(' ')))

a=[line1,line2,line3,line4]

total=0
for i in range(4):
    for j in range(i+1):
        total+=a[i][j]
print(total)