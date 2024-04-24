n = int(input())

start = 1
while n>1:
    start+=1
    n//=start
    
print(start)