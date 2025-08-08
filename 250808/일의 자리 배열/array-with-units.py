nums = list(map(int, input().split(' ')))

length = 10

for i in range(length-2):
    n1 = nums[i]
    n2 = nums[i+1]

    next_n = (n1+n2)%10
    nums.append(next_n)

for n in nums:
    print(n,end=' ')

