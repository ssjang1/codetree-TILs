n,m = map(int,input().split(' '))

def find_gcd(n,m):
    value =1
    for i in range(1,min(n,m)+1):
        if n%i ==0 and m%i==0:
            value = i
    return value

print(find_gcd(n,m))