n = int(input())

arr = list(map(int,input().strip().split(' ')))

arr.sort()
for a in arr:
    print(a,end=' ')

print()

arr.sort(reverse=True)
for a in arr:
    print(a,end=' ')