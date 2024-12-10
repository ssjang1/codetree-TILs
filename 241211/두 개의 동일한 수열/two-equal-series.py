n = int(input())

A = list(map(int,input().strip().split(' ')))
B = list(map(int,input().strip().split(' ')))

A.sort()
B.sort()

ans = A == B
if ans:
    print("Yes")
else:
    print("No")