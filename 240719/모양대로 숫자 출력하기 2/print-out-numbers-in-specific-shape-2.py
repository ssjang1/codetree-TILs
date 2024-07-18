n = int(input())

check = 2
for i in range(n):
    for j in range(n):
        print(check,end=' ')
        check+=2
        if check==10:
            check=2
    print()