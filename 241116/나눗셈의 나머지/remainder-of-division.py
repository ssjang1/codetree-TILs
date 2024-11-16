a,b = map(int,input().split(' '))
check = []
while a >1:
    remain = a%b
    check.append(remain)
    a=a//b
result = 0
for i in set(check):
    result += check.count(i)**2

print(result)