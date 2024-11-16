n = int(input())

line = list(map(int,input().strip().split(' ')))

maxi =0
for i in range(n):
    for j in range(i,n):
        if line[j]-line[i]>maxi:
            maxi = line[j]-line[i]

print(maxi)