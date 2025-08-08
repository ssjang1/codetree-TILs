A,B = map(int,input().split(' '))

s = 0

for num in range(A,B+1):
    if num%2 == 0:
        s += num

print(s)