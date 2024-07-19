start, end = map(int, input().split(' '))

def check(number):
    cnt = 0
    for i in range(1,number+1):
        if number % i ==0:
            cnt +=1

    if cnt >=4:
        return False
    if cnt <=2:
        return False
    return True
cnt = 0
for i in range(start, end+1):
    cnt+= check(i)
print(cnt)