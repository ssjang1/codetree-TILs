n= int(input())

if n%2 == 1:
    m=n-1
else:
    m=n

now = int(n/2)
for i in range(1,n+1):
    if i ==1:
        print(' '.join('*'*n))
    elif i==2:
        print(' '*2,end='')
        print('   '.join('*'*now))
        now -= 1
    else:
        print(' '*(2*m-4*now+2),end='')
        print('   '.join('*'*now))
        now -= 1