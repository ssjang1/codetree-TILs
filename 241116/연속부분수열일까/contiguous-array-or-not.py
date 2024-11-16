n1,n2=map(int,input().split(' '))

a = list(map(int,input().strip().split(' ')))
b = list(map(int,input().strip().split(' ')))

indices = [i for i, value in enumerate(a) if value == b[0]]

check =0
for i in indices:
    if a[i:i+len(b)] == b:
        check +=1

if check:
    print("Yes")
else:
    print("No")