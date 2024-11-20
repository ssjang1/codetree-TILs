a, b = map(int,input().strip().split(' '))

def answer(a,b):
    if a >= b :
        a += 25
        b *= 2
    else:
        b += 25
        a *= 2
    return a,b

a,b = answer(a,b)
print(a,b,end=' ')
    