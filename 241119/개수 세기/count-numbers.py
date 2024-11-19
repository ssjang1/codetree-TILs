n, m = map(int, input().strip().split(' '))

numbers = list(map(int,input().strip().split(' ')))
cnt =0
for num in numbers:
    if num == m:
        cnt +=1

print(cnt)