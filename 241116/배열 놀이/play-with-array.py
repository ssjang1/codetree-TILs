n,q = map(int,input().split(' '))
wonso = list(map(int,input().strip().split(' ')))

for i in range(q):
    line = list(map(int,input().split(' ')))
    if line[0] == 1:
        print(wonso[line[1]-1])
    elif line[0] ==2:
        if line[1] in wonso:
            print(wonso.index(line[1])+1)
        else:
            print(0)
    elif line[0] ==3:
        for i in range(line[1]-1,line[2]):
            print(wonso[i],end=' ')
        print()
