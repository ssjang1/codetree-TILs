n = int(input())
for i in range(1,n+1):
    start =11
    start += 2*i-2
    for j in range(n):
        print(start,end=' ')
        start +=2
    print()