def is_onjun(n):
    strn = str(n)
    if n % 2==0:
        return False
    if strn[-1]=='5':
        return False
    if n%3==0 and n%9!=0:
        return False
    return True

a,b = map(int,input().strip().split(' '))
cnt=0
for i in range(a,b+1):
    if is_onjun(i):
        cnt+=1

print(cnt) 