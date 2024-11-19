s,q = input().split(' ')
q = int(q)

for i in range(q):
    a,b,c = input().split(' ')
    if a =='1':
        b = int(b)
        c = int(c)
        check = list(s)
        check[b-1], check[c-1] = check[c-1], check[b-1]
        result = ''.join(check)
        print(result)
    elif a=='2':
        s = s.replace(b,c)
        print(s)