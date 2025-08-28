n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

check =[0 for i in range(200)]

for x1, x2 in segments:
    for i in range(x1, x2):
        check[i] += 1

print(max(check))        

