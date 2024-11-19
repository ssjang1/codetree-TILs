line = input()

ee=0
eb=0

for i in range(0,len(line)-1):
    if line[i]=='e' and line[i+1]=='b':
        eb+=1
    elif line[i]=='e' and line[i+1]=='e':
        ee+=1

print(ee,eb,end=' ')