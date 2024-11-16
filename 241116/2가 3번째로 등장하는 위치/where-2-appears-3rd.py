n = int(input())
a = list(map(int,input().strip().split(' ')))

indices = [i for i,v in enumerate(a) if v==2]
print(indices[2]+1)