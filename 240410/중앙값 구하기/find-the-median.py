a,b,c = map(int, input().split())

if (a-b) * (a-c) <0:
    print(a)
elif (b-a) * (b-c) <0:
    print(b)
else:
    print(c)