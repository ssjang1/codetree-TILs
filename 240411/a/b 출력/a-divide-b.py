# import math

a,b = map(int, input().split(' '))

# c = a/b

# c *= 10**20
# c = math.floor(c)
# c /= 10**20

# print(f"{c:.21f}")

mok = str(a//b)+'.'
a = a%b * 10

for i in range(20):
    c = a//b 
    a = a%b *10
    mok += str(c)

print(mok)