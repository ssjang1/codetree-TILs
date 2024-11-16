a,b = map(int,input().split(' '))
check = []
while a >=1:
    a=a//b
    remain = a%b
    check.append(remain)

result = 0
for i in set(check):
    result += check.count(i)**2

print(result)