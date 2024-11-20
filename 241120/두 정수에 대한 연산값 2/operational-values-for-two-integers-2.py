a,b = map(int,input().strip().split(' '))

def answer(a,b):
    if a>=b:
        a *=2
        b +=10
    else:
        b *=2
        a+=10
    return a,b

answer(a,b)
print(a,b,end=' ')
