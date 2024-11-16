a,b,c,d,e = 0,0,0,0,0
for i in range(3):
    cold, temperature = input().split(' ')
    temp = float(temperature)
    if cold == "Y" and temp >=37:
        a+=1
    elif cold == "N" and temp >=37:
        b+=1
    elif cold =="Y" and temp <37:
        c+=1
    else:
        d+=1
    
if a>=2:
    e+=1

print(a,end=' ')
print(b,end=' ')
print(c,end=' ')
print(d,end=' ')
if e:
    print("E")