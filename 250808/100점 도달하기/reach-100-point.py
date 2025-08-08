N= int(input())

def check(n):
    grade = ''
    if n>=90:
        grade='A'
    elif n>=80:
        grade='B'
    elif n>=70:
        grade='C'
    elif n>=60:
        grade='D'
    else:
        grade='F'
    return grade

for n in range(N,101):
    print(check(n),end=' ')