n = int(input())

def check(n):
    if n ==1:
        return 1
    if n==2:
        return 2
    return check(int(n/3))+check(n-1)

print(check(n))