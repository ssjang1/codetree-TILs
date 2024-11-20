n = int(input())

def jegob(n):
    if n < 10:
        return n**2
    return jegob(n//10) + (n%10)**2

print(jegob(n))