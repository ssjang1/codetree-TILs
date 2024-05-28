N = int(input())

c=0
while True:
    if 2**c == N:
        print(c)
        break
    else:
        c+=1