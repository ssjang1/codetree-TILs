def hap(a,b):
    return a+b
def cha(a,b):
    return a-b
def nanugi(a,b):
    return int(a/b)
def gob(a,b):
    return a*b

a,o,c = input().strip().split(' ')
a,c = map(int,[a,c])
def sa4(a,o,c):
    if o not in ['+','-','/','*']:
        print('False')
    elif o == '+':
        print(a,o,c,'=',hap(a,c),end=' ')
    elif o == '-':
        print(a,o,c,'=',cha(a,c),end=' ')
    elif o == '/':
        print(a,o,c,'=',nanugi(a,c),end=' ')
    elif o == '*':
        print(a,o,c,'=',gob(a,c),end=' ')

sa4(a,o,c)