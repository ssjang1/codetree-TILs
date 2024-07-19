n = int(input())

check =1
for i in range(n):
    for j in range(i+1):
        print(check,end=' ')
        check +=1
    print()