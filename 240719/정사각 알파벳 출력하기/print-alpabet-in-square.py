n = int(input())

start = ord('A')

for i in range(n):
    for j in range(n):
        print(chr(start),end=' ')
        start +=1
    print()