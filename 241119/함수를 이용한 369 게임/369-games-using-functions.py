def find_369_target(n,m):
    cnt = 0
    for i in range(n,m+1):
        strn=str(i)
        if '3' in strn or '6' in strn or '9' in strn or i%3==0:
            cnt+=1
    return cnt

n,m = map(int,input().strip().split(' '))
print(find_369_target(n,m))
