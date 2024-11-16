n = int(input())

line = list(map(int,input().strip().split(' ')))

unique_line = [i for i in line if line.count(i)==1]

if unique_line:
    print(max(unique_line))
else:
    print(-1)