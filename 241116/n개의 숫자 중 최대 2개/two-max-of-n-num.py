n = int(input())
a = list(map(int,input().strip().split(' ')))

b = a.sort(reverse=True)

print(b[0],b[1],end=" ")