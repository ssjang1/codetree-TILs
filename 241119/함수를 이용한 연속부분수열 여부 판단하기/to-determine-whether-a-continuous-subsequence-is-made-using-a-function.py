n1, n2 = map(int, input().strip().split(' '))

a = list(map(int,input().strip().split(' ')))
b = list(map(int,input().strip().split(' ')))

def bubun(a,b):
    len_a = len(a)
    len_b = len(b)
    if len_b>len_a:
        return False
    start = b[0]
    for i in range(len_a):
        if a[i]==start:
            if a[i:i+len_b] == b:
                return True
    return False

if bubun(a,b):
    print('Yes')
else:
    print('No')