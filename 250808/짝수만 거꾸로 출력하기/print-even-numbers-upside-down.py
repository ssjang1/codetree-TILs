N = int(input())

nums = list(map(int,input().strip().split(' ')))

for i in range(-1,-len(nums)-1,-1):
    if nums[i]%2==0:
        print(nums[i],end=' ')