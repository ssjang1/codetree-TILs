n = int(input())

def pro(n):
    cnt = 0
    if n ==1:
        return cnt
    cnt += 1
    if n%2 ==0:
        return pro(n//2) + cnt
    else:
        return pro(n//3) + cnt

print(pro(n))