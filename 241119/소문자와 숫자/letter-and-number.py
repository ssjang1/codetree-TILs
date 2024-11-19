line = input()

for i in line:
    if i.isalpha():
        print(i.lower(),end='')
    elif i.isdigit():
        print(i,end='')