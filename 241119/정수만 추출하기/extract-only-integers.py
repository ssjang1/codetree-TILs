a,b = input().strip().split(' ')

A = ''
B = ''

for i in a:
    if i.isdigit():
        A += i
    else:
        break

for i in b:
    if i.isdigit():
        B += i
    else:
        break

print(int(A)+int(B))