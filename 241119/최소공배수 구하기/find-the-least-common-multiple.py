def gcd(n,m):
    for i in range(1,min(n,m)+1):
        if n%i==0 and m%i==0:
            value = i
    return value

def lcm(n,m):
    value = n*m/gcd(n,m)
    return value

n,m = map(int, input().strip().split(' '))

print(int(lcm(n,m)))