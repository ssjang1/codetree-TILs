line1 = list(map(int,input().strip().split(' ')))
line2 = list(map(int,input().strip().split(' ')))
print(sum(line1)/len(line1),sum(line2)/len(line2),end =' ')
print()
for i in range(len(line1)):
    print((line1[i]+line2[i])/2, end=' ')
print()
print(round((sum(line1)+sum(line2))/8,1))