M,D = map(int,input().strip().split(' '))

def check(M,D):
    if M in [2]:
        if 1<= D <= 28:
            print("Yes")
        else:
            print("No")
    elif M in [1,3,5,7,8,10,12]:
        if 1<=D<=31:
            print("Yes")
        else:
            print("No")
    elif M in [4,6,9,11]:
        if 1<=D<=30:
            print("Yes")
        else:
            print("No")

check(M,D)