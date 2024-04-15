a,b = map(int, input().split(' '))

s = 0

if a> b:
    a,b = b,a

for i in range(a, b+1):
    if i%5==0:
        s += i

print(s)