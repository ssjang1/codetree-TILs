n = int(input())

s = 0
for i in range(n):
    a = int(input())
    if a%2==1 and a%3==0:
        s+=a

print(s)