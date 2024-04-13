n = int(input())

for i in range(1,n+1):
    if i % 3 ==0 or '3' in list(str(i)) or '6' in list(str(i)) or '9' in list(str(i)):
        print(0, end=' ')
    else:
        print(i, end =' ')