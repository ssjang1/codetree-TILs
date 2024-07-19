n = int(input())

def sosu(number):
    cnt = 0
    for i in range(1,int(number**0.5)+1):
        if number % i ==0:
            cnt +=1
    if cnt != 1:
        return False
    if number == 1:
        return False
    return True

for i in range(1,n+1):
    if sosu(i):
        print(i,end=' ')