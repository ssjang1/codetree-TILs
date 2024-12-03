n = int(input())

def su(n):
    if n ==1:
        return 2
    if n ==2:
        return 4
    return (su(n-2)*su(n-1))%100

print(su(n))