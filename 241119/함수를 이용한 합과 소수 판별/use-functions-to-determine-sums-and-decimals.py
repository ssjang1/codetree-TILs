def sosu(n):
    if n==1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

def jari_hap_even(n):
    result = 0
    strn = str(n)
    for s in strn:
        result += int(s)
    return result%2==0

a,b = map(int,input().strip().split(' '))
cnt =0
for i in range(a,b+1):
    if sosu(i) and jari_hap_even(i):
        cnt +=1
print(cnt)