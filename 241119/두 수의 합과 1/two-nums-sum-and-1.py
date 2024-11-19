a,b = map(int,input().strip().split(' '))

word = str(a+b)
cnt = 0
for w in word:
    if w == '1':
        cnt+=1

print(cnt)