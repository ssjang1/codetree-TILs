Y,M,D = map(int,input().strip().split(' '))

def yoon(Y):
    if Y % 400 == 0:
        return True
    elif Y % 100 == 0:
        return False
    elif Y % 4 == 0:
        return True
    else:
        return False

def is_valid(Y,M,D):
    if not yoon(Y):
        if M in [2]:
            if 1<= D <= 28:
                return True
            else:
                return False
        elif M in [1,3,5,7,8,10,12]:
            if 1<=D<=31:
                return True
            else:
                return False
        elif M in [4,6,9,11]:
            if 1<=D<=30:
                return True
            else:
                return False
        else:
            return False
    elif yoon(Y):
        if M in [2]:
            if 1<= D <= 29:
                return True
            else:
                return False
        elif M in [1,3,5,7,8,10,12]:
            if 1<=D<=31:
                return True
            else:
                return False
        elif M in [4,6,9,11]:
            if 1<=D<=30:
                return True
            else:
                return False
        else:
            return False

def answer(Y,M,D):
    if not is_valid(Y,M,D):
        print(-1)
    elif is_valid(Y,M,D):
        if 3<=M<=5:
            print("Spring")
        elif 6<=M<=8:
            print("Summer")
        elif 9<=M<=11:
            print("Fall")
        elif M in [1,2,12]:
            print('Winter')
        else:
            print(-1)

answer(Y,M,D)