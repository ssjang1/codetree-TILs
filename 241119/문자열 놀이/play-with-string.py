s,q = input().split(' ')
q = int(q)

for i in range(q):
    a,b,c = input().split(' ')
    if a =='1':
        b = int(b)
        c = int(c)
        check = list(s)
        char1 = check[b-1]
        char2 = check[c-1]
        check[b-1] = char2 
        check[c-1] = char1

        s = ''.join(check)
        print(s)
    elif a=='2':
        s = s.replace(b,c)
        print(s)


