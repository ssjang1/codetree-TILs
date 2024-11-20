line1= input()
line2= input()

def check(line1,line2):
    if line2 in line1:
        print(line1.index(line2))
    else:
        print(-1)

check(line1,line2)