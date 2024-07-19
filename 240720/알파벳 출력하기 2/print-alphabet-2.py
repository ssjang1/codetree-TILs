n = int(input())

start = ord('A')
finish = ord('Z')
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print(chr(start), end=' ')
        start +=1
        if start == finish+1:
            start= ord('A')
    print()