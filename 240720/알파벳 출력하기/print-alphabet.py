n = int(input())

start = ord('A')
finish = ord('Z')

for i in range(n):
    for j in range(i+1):
        print(chr(start),end='')
        start +=1
        if start == finish:
            start = ord('A')
    print()