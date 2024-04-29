n=0
while n!=25:
    n=int(input())
    if n>25:
        print('Lower')
    elif n<25:
        print('Higher')
    else:
        print('Good')
        break