n1,n2,n3 = map(int,input().strip().split(' '))

def digit_sum(n):
    if n <10:
        return n
    else:
        return (n%10) + digit_sum(n//10)

print(digit_sum(n1*n2*n3))