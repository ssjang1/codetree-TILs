n = int(input())
a = list(map(int,input().strip().split(' ')))

b = sorted(a,reverse=True)

print(b[0],b[1],end=" ")