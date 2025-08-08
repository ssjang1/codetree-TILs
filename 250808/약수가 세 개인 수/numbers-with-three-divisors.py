start, end = map(int, input().split())

# Please write your code here.

def yak(n):
    s = 0
    for i in range(1,n+1):
        if n%i ==0:
            s +=1
    return s

s3 = 0
for i in range(start,end+1):
    if yak(i) == 3:
        s3 += 1

print(s3)