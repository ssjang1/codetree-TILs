n = int(input())

check = 1
for i in range(n):
    print((' '+' ')*i,end='')
    for j in range(n-i):
        print(check, end=' ')
        check +=1
        if check >=10:
            check =1
    print()