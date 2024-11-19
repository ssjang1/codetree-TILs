y = int(input())

def find_yoon_year(n):
    if y%100==0 and y%400 !=0:
        return False
    elif y%4==0:
        return True
    else:
        return False

if find_yoon_year(y):
    print('true')
else:
    print('false')