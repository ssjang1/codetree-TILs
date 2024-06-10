a,b= map(int,input().split(' '))

check = False

for i in range(2,a+1):
    if a%i==0 and b%i==0:
        check=True
        break

if check:
    print(1)
else:
    print(0)