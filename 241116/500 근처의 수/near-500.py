line = list(map(int,input().strip().split(' ')))

under500 = [i for i in line if i <500]
upper500 = [i for i in line if i >=500]

print(max(under500),min(upper500),end=" ")