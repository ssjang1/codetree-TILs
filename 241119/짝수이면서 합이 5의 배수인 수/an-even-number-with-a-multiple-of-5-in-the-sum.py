def magic_number(n):
    hap = int(str(n)[0]) + int(str(n)[1])
    if n%2==0 and hap%5 ==0:
        print("Yes")
    else:
        print("No")

n= int(input())
magic_number(n)