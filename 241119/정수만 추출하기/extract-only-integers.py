a,b = input().strip().split(' ')

A = ''
B = ''

for i in a:
    if a.isdigit():
        A +=a
    else:
        break

for i in b:
    if b.isdigit():
        B +=b
    else:
        break

print(int(A)+int(B))