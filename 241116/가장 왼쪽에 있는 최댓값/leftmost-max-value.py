n = int(input())
line = list(map(int,input().strip().split(' ')))

while len(line)>0:
    print(line.index(max(line))+1,end=" ")
    line = line[:line.index(max(line))]
    