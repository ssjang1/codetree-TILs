N = int(input())

nums = list(map(int,input().strip().split(' ')))

for n in nums:
    print(n*n,end=' ')