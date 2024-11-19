line1 = input()
line2 = input()

a,b ='',''

for i in line1:
    if i.isdigit():
        a+=i
for i in line2:
    if i.isdigit():
        b+=i

print(int(a)+int(b))