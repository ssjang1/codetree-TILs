n = int(input())

start = 9
for i in range(n):
    for j in range(n):
        print(start, end='')
        start -=1
        if start ==0:
            start =9
    print()