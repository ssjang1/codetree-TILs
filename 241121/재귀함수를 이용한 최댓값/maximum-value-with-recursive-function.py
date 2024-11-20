n = int(input())

a = list(map(int,input().strip().split(' ')))

def find_maxi(a):
    if len(a) == 1:
        return a[0]
    rest = a[1:]
    return a[0] if a[0] > find_maxi(rest) else find_maxi(rest)

print(find_maxi(a))