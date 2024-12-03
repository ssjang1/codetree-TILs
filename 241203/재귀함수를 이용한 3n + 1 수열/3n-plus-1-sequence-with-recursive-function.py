n = int(input())

def check(n,count=-1):
    count+=1
    if n == 1:
        return count
    else:
        if n%2 ==0:
            return check(int(n/2),count)
        else:
            return(check(3*n+1,count))

print(check(n))