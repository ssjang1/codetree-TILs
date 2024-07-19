start, end = map(int,input().split(' '))

def check(number):
    sum = 0
    for i in range(1,number):
        if number %i==0:
            sum += i
    return sum
cnt = 0
for i in range(start, end+1):
    if i==check(i):
        cnt +=1

print(cnt)