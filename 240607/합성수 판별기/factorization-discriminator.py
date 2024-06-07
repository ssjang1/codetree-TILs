n = int(input())

a = False
for i in range(2,n):
    if n%i ==0:
        a = True

if a:
    print('C')
else:
    print('N')